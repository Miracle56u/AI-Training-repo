import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)


def llm_tool(state):

    response = llm.invoke(
        state["question"]
    )

    return {
        "answer": response.content
    }