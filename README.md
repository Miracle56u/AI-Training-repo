# LangGraph Multi-Tool Agent

## Overview

This project demonstrates the core concepts of LangGraph by building a simple AI agent capable of routing user requests to different tools based on the input.

The agent uses three tools:

1. Calculator Tool – Performs basic arithmetic calculations.
2. Weather Tool – Retrieves real-time weather information using the OpenWeatherMap API.
3. LLM Tool – Uses OpenAI to answer general questions.

The purpose of this project is to understand how LangGraph manages state, nodes, edges, and conditional routing while integrating external tools and Large Language Models (LLMs).

---

## Project Structure

```text
day3-langgraph-agent/
│
├── langgraph_agent.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── tools/
    ├── __init__.py
    ├── calculator.py
    ├── weather.py
    └── llm_tool.py
```

---

## LangGraph Concepts Demonstrated

### Nodes

Nodes represent individual actions or processing steps in the graph.

In this project:

- Router Node
- Calculator Tool Node
- Weather Tool Node
- LLM Tool Node

---

### State

State is the shared data passed between nodes.

The application uses the following state:

```python
class State(TypedDict):
    question: str
    route: str
    answer: str
```

---

### Edges

Edges define how execution moves between nodes.

Examples:

```text
Router → Calculator
Router → Weather
Router → LLM
```

---

### Conditional Routing

The Router node examines the user input and determines which tool should handle the request.

Examples:

| User Input | Route |
|------------|--------|
| 25 * 8 | Calculator |
| weather in Lagos | Weather |
| What is Terraform? | LLM |

---

## Agent Workflow

```text
                User Input
                     │
                     ▼
                ┌────────┐
                │ Router │
                └────┬───┘
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 Calculator     Weather Tool     LLM Tool
      │              │              │
      └──────────────┴──────────────┘
                     │
                     ▼
               Final Answer
```

---

## Tool Descriptions

### Calculator Tool

Purpose:
- Detects and evaluates simple arithmetic expressions.

Example:

Input:

```text
50 * 10
```

Output:

```text
50 * 10 = 500
```

---

### Weather Tool

Purpose:
- Retrieves real-time weather information from OpenWeatherMap.

Example:

Input:

```text
weather in Lagos
```

Output:

```text
Lagos: 29°C, scattered clouds
```

---

### LLM Tool

Purpose:
- Handles all general-purpose questions using OpenAI.

Example:

Input:

```text
Explain Terraform
```

Output:

```text
Terraform is an Infrastructure as Code tool...
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd day3-langgraph-agent
```

---

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

Git Bash:

```bash
source venv/Scripts/activate
```

Command Prompt:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_weather_api_key
```

---

### 5. Run the Agent

```bash
python langgraph_agent.py
```

---

## Example Usage

Calculator:

```text
You: 25 * 8

Agent: 25 * 8 = 200
```

Weather:

```text
You: weather in London

Agent: London: 18°C, light rain
```

General Question:

```text
You: What is Kubernetes?

Agent: Kubernetes is a container orchestration platform...
```

---

## Technologies Used

- Python
- LangGraph
- LangChain
- OpenAI API
- OpenWeatherMap API
- Requests
- Python Dotenv

---

## Learning Outcomes

Through this project, the following LangGraph concepts were explored:

- Graph-based AI workflows
- State management
- Node creation
- Conditional routing
- Tool integration
- External API consumption
- LLM integration

This project serves as a foundational example of building AI agents using LangGraph and demonstrates how different tools can be orchestrated within a graph-based workflow.
