import pandas as pd

df = pd.read_csv("results/runs.csv")

print("\n=== LLM PERFORMANCE SUMMARY ===\n")

# Group by model
grouped = df.groupby("model")

summary = grouped.agg({
    "latency": "mean",
    "tokens": "sum"
})

print(summary)

print("\n=== PROMPT BREAKDOWN ===\n")

for prompt in df["prompt"].unique():
    print(f"\nPROMPT: {prompt}")
    temp = df[df["prompt"] == prompt][["model", "latency", "tokens"]]
    print(temp)