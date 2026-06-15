import os
import time
import csv
import json
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

PROMPTS = [
    "Explain Terraform in simple terms.",
    "What is CI/CD in DevOps?",
    "Explain Docker vs Kubernetes simply."
]

RESULTS_FILE = "results/runs.csv"


def call_openai(prompt):
    start = time.time()
    try:
        res = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        end = time.time()

        return {
            "model": "openai",
            "text": res.choices[0].message.content,
            "latency": end - start,
            "tokens": res.usage.total_tokens
        }

    except Exception as e:
        return {"model": "openai", "text": str(e), "latency": None, "tokens": 0}


def call_anthropic(prompt):
    start = time.time()

    res = anthropic_client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )

    end = time.time()

    usage = res.usage

    return {
        "model": "anthropic",
        "text": res.content[0].text,
        "latency": end - start,
        "tokens": usage.input_tokens + usage.output_tokens
    }


def save_csv(row):
    file_exists = os.path.isfile(RESULTS_FILE)

    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(row)


def main():
    print("\n=== LLM BENCHMARK PRO RUN ===\n")

    all_results = []

    for prompt in PROMPTS:
        print(f"\nPROMPT: {prompt}\n")

        oai = call_openai(prompt)
        claude = call_anthropic(prompt)

        all_results.extend([oai, claude])

        for r in [oai, claude]:
            save_csv({
                "timestamp": datetime.now(),
                "model": r["model"],
                "prompt": prompt,
                "latency": r["latency"],
                "tokens": r["tokens"],
                "response": r["text"][:200]
            })

            print(f"\n--- {r['model'].upper()} ---")
            print(r["text"])
            print(f"Latency: {r['latency']}")
            print(f"Tokens: {r['tokens']}")

    print("\nDONE. Results saved to CSV.")


if __name__ == "__main__":
    main()