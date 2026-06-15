# LLM Comparison Report

## 1. Objective
Compare OpenAI and Anthropic models based on latency, token usage, and response quality.

---

## 2. Models Tested
- OpenAI GPT-4o-mini
- Anthropic Claude Sonnet 4.5

---

## 3. Evaluation Metrics
- Response latency (seconds)
- Token usage
- Qualitative response clarity

---

## 4. Methodology
- Three identical DevOps prompts were used:
Terraform explanation
CI/CD in DevOps
Docker vs Kubernetes comparison
- Both models were queried using API calls
- Latency measured using Python execution time
- Token usage extracted from API responses
- Results logged into CSV for analysis

---

## 5. Performance Results
- Latency Comparison (Average)

- OpenAI:
9.61s
11.31s
5.07s
Average ≈ 8.67s

- Anthropic:
9.32s
8.82s
8.30s
Average ≈ 8.81s

- Token Usage
- OpenAI:
298 + 584 + 265 = 1147 tokens total

- Anthropic:
372 + 376 + 278 = 1026 tokens total

---

## 6. Quality Comparison (Observations)
# OpenAI GPT-4o-mini
- Very clear and structured explanations
- Strong educational breakdown style
- Slightly more verbose in responses
- Good at step-by-step teaching

# Anthropic Claude Sonnet 4.5
- More concise and structured formatting
- Strong use of analogies (especially Docker vs Kubernetes)
- Better readability for quick understanding
- Slightly more efficient token usage

---

## Recommended Use Cases
# OpenAI GPT-4o-mini
- Detailed technical explanations
- Learning-focused content
- Step-by-step DevOps breakdowns

# Anthropic Claude Sonnet 4.5
- Quick architectural summaries
- Documentation writing
- Conceptual simplification using analogies

---

## Conclusion
Both models performed closely in latency and quality. OpenAI produced more detailed and educational responses, while Anthropic produced more concise and structured explanations with slightly better token efficiency.

---

## Overall:
- Best for depth: OpenAI GPT-4o-mini
- Best for clarity & conciseness: Anthropic Claude Sonnet 4.5
- Performance difference: minimal in real DevOps-style prompts

## 7. Dataset
All results stored in:
results/runs.csv