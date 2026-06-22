# Day 3 - LangChain & LangGraph Project

## Overview
This project demonstrates basic usage of LangChain and LangGraph for LLM application development.

---

## 1. LangChain Chain

### File: langchain_chain.py

### What it does:
- Takes a user question
- Sends it to an LLM using a prompt template
- Returns a structured response

### Flow:
User → PromptTemplate → OpenAI LLM → Output

---

## 2. LangGraph Agent

### File: langgraph_agent.py

### What it does:
- Routes input based on keywords
- Sends request to different tools
- Returns final answer

### Flow:
User → Router → Tool A (DevOps) OR Tool B (General) → Output

---

## Key Concepts

### LangChain
- Chains
- Prompt Templates
- LLM wrappers

### LangGraph
- Nodes (functions)
- Edges (flow connections)
- State (shared data)
- Conditional routing

---

## How to run

```bash
python langchain_chain.py
python langgraph_agent.py