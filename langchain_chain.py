from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful DevOps assistant."),
    ("user", "{question}")
])

# Chain
chain = prompt | llm | StrOutputParser()

# Run
if __name__ == "__main__":
    question = "What is Terraform in simple terms?"
    response = chain.invoke({"question": question})

    print("\n=== LANGCHAIN RESPONSE ===\n")
    print(response)