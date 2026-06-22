import os
from dotenv import load_dotenv

from openai import OpenAI
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# Initialize clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

PROMPT = "Reply with: API connection successful"

def test_openai():
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": PROMPT}]
        )
        print("\n✅ OpenAI Response:")
        print(response.choices[0].message.content)
    except Exception as e:
        print("\n❌ OpenAI Error:")
        print(e)


def test_anthropic():
    try:
        response = anthropic_client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=50,
            messages=[{"role": "user", "content": PROMPT}]
        )
        print("\n✅ Anthropic Response:")
        print(response.content[0].text)
    except Exception as e:
        print("\n❌ Anthropic Error:")
        print(e)


def main():
    print("\n=== TESTING OPENAI & ANTHROPIC APIs ===")

    test_openai()
    test_anthropic()

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()