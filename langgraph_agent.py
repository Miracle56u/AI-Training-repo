from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

# State
class State(TypedDict):
    question: str
    route: str
    answer: str


# Router node
def router(state: State):
    q = state["question"].lower()

    if "terraform" in q or "devops" in q or "docker" in q:
        return {"route": "devops"}
    else:
        return {"route": "general"}


# Tool A
def devops_tool(state: State):
    response = llm.invoke(
        f"Explain this DevOps topic simply: {state['question']}"
    )
    return {"answer": response.content}


# Tool B
def general_tool(state: State):
    response = llm.invoke(
        f"Explain simply: {state['question']}"
    )
    return {"answer": response.content}


# Routing logic
def route_decision(state: State) -> Literal["devops", "general"]:
    return state["route"]


# Build graph
graph = StateGraph(State)

graph.add_node("router", router)
graph.add_node("devops", devops_tool)
graph.add_node("general", general_tool)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    route_decision,
    {
        "devops": "devops",
        "general": "general"
    }
)

graph.add_edge("devops", END)
graph.add_edge("general", END)

app = graph.compile()


# Run
if __name__ == "__main__":
    result = app.invoke({
        "question": "What is Docker and how does it work?"
    })

    print("\n=== LANGGRAPH RESPONSE ===\n")
    print(result["answer"])