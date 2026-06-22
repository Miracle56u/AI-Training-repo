from typing import TypedDict, Literal

from langgraph.graph import StateGraph, END

from tools.calculator import calculator_tool
from tools.weather import weather_tool
from tools.llm_tool import llm_tool

import re


class State(TypedDict):
    question: str
    route: str
    answer: str


# Router
def router(state: State):

    question = state["question"].lower()

    # Calculator Route
    if re.search(
        r"\d+\s*[\+\-\*/]\s*\d+",
        question
    ):
        return {
            "route": "calculator"
        }

    # Weather Route
    if "weather" in question:
        return {
            "route": "weather"
        }

    # Default Route
    return {
        "route": "llm"
    }


# Conditional Edge
def route_decision(
    state: State
) -> Literal[
    "calculator",
    "weather",
    "llm"
]:
    return state["route"]


# Graph
graph = StateGraph(State)

graph.add_node(
    "router",
    router
)

graph.add_node(
    "calculator",
    calculator_tool
)

graph.add_node(
    "weather",
    weather_tool
)

graph.add_node(
    "llm",
    llm_tool
)

graph.set_entry_point(
    "router"
)

graph.add_conditional_edges(
    "router",
    route_decision,
    {
        "calculator": "calculator",
        "weather": "weather",
        "llm": "llm"
    }
)

graph.add_edge(
    "calculator",
    END
)

graph.add_edge(
    "weather",
    END
)

graph.add_edge(
    "llm",
    END
)

app = graph.compile()


if __name__ == "__main__":

    print(
        "\nLangGraph Agent Started"
    )

    while True:

        question = input(
            "\nYou: "
        )

        if question.lower() in [
            "quit",
            "exit"
        ]:
            break

        result = app.invoke(
            {
                "question": question
            }
        )

        print(
            "\nAgent:",
            result["answer"]
        )