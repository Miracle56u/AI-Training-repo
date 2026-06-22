import re


def calculator_tool(state):

    question = state["question"]

    expression = re.search(
        r"(\d+\s*[\+\-\*/]\s*\d+)",
        question
    )

    if not expression:
        return {
            "answer": "No valid calculation found."
        }

    result = eval(expression.group(1))

    return {
        "answer": f"{expression.group(1)} = {result}"
    }