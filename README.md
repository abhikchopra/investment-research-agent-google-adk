# Investment Research Agent - Google ADK

A multi-agent investment research system built using Google ADK, Vertex AI (Gemini), Docker, and Cloud Run.

This repository focuses on two core agentic AI concepts:

1. Multi-Agent Collaboration
2. Tool Calling & Explainability

---

## Learning Progression

### Day 1

Multi-Agent Workflow

```text
Question
   ↓
Planner
   ↓
Research
   ↓
Analyst
   ↓
Writer
```

Goal:

Learn how multiple specialized agents collaborate to solve a business problem.

---

### Day 2

Tool Calling + Explainability

```text
Question
   ↓
Planner
   ↓
Research
   ├── Search Tool
   ├── Calculator Tool
   └── (Future Retriever Tool)
   ↓
Analyst
   ↓
Writer
   ↓
Explainability
```

Goal:

Transform a simple multi-agent demo into a production-style AI workflow that can:

* Use external tools
* Ground responses
* Track sources
* Explain recommendations
* Provide auditability

---

## Business Problem

Analyze a company as an investment opportunity and produce a professional investment report.

Example:

```text
Analyze Microsoft as an investment opportunity.
```

Output:

```text
Executive Summary

Bull Case

Bear Case

Risks

Recommendation

Sources Used

Tools Used

Agent Contributions

Confidence Score
```

---

## Architecture

```text
User Question
      ↓

Planner Agent
      ↓

Research Agent
      │
      ├── Google Search Tool
      ├── Calculator Tool
      └── Future Retriever Tool

      ↓

Analyst Agent
      ↓

Writer Agent
      ↓

Explainability Agent
      ↓

Final Investment Report
```

---

## Day 2 Scope

The original objective was to introduce three tools and an explainability layer.

### Search Tool

Why?

Day 1 relied entirely on Gemini's internal knowledge.

Problems:

* Potentially outdated information
* No citations
* No source tracking
* No grounding

The solution was to introduce Google's built-in search capability through ADK.

Learning objectives:

* Tool Calling
* Grounding
* Source Attribution

Example research queries:

* Microsoft latest earnings
* Microsoft annual report
* Microsoft investor presentation
* Microsoft AI strategy

Expected sources:

* Annual Reports
* Earnings Calls
* Investor Presentations
* Company Websites

---

### Calculator Tool

Purpose:

Demonstrate deterministic tool execution.

LLMs are not reliable calculators.

A tool is.

Examples:

* CAGR
* Revenue Growth
* Margin Analysis
* P/E Ratio
* Valuation Scenarios

Implementation:

```python
def calculator_tool(expression: str):

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Calculation error: {str(e)}"
```

Examples:

```text
100 * (1.15 ** 5)

Revenue growth at 15% annually for 5 years
```

---

### Retriever Tool (Planned)

Original intention:

```text
PDF
 ↓
Chunking
 ↓
Embeddings
 ↓
FAISS
 ↓
Retriever Tool
 ↓
Research Agent
```

Target documents:

* Annual Reports
* Investor Presentations
* SEC Filings
* 10-K Reports

Example:

Question:

What are Microsoft's AI growth drivers?

Retriever returns:

Page 17

Azure AI Growth

Copilot Revenue Growth

Research Agent incorporates findings into analysis.

Reason for Choosing FAISS:

* Already learned in Week 1
* Focus remained on Tool Calling
* Avoid unnecessary vector database complexity

Status:

Deferred.

The repository already demonstrated Tool Calling through Search and Calculator tools, making Retriever lower priority.

---

## Explainability Layer

Most AI demos stop here:

```text
Question
 ↓
Answer
```

Production systems require:

```text
Question
 ↓
Answer
 ↓
Why?
```

Day 2 introduced explainability.

---

### Sources Used

Example:

```text
Microsoft Annual Report

Microsoft Investor Presentation

Microsoft Earnings Call
```

Purpose:

Transparency

Auditability

Trust

---

### Tools Used

Example:

```text
Google Search Tool

Calculator Tool
```

Purpose:

Understand how conclusions were generated.

---

### Agent Contributions

Example:

Planner Agent

Created research framework

Research Agent

Collected evidence

Analyst Agent

Performed investment analysis

Writer Agent

Generated recommendation

Purpose:

Agent observability.

---

### Key Findings

Example:

```text
Azure growth remains strong

AI investments accelerating

Strong cash position

Regulatory risk remains
```

Purpose:

Explain major drivers behind the recommendation.

---

### Confidence Score

Original design:

Research Agent outputs:

```text
Evidence Strength

High
Medium
Low
```

Analyst maps:

```text
High   → 9
Medium → 7
Low    → 5
```

Writer generates:

```text
Confidence Score: 8.4 / 10
```

Goal:

Avoid arbitrary confidence values.

---

## Final Report Structure

Day 2 report structure:

```text
Executive Summary

Bull Case

Bear Case

Risks

Key Findings

Sources Used

Tools Used

Agent Contributions

Confidence Score

Final Recommendation
```

---

## Technology Stack

### AI

* Google ADK
* Vertex AI
* Gemini 2.5 Flash

### Agent Framework

* SequentialAgent
* Tool Calling
* Multi-Agent Collaboration

### Backend

* FastAPI
* Uvicorn

### Infrastructure

* Docker
* Google Cloud Run
* Artifact Registry

### Development

* Python
* GitHub

---

## What Was Built

Completed:

✓ Multi-Agent Workflow

✓ Search Tool

✓ Calculator Tool

✓ Explainability Layer

✓ Sources Tracking

✓ Tools Tracking

✓ Agent Contribution Tracking

✓ Docker Deployment

✓ Cloud Run Deployment

---

## What Was Deferred

Deferred:

✓ Retriever Tool (FAISS-based)

Reason:

The learning objective of Day 2 was Tool Calling and Explainability, not RAG or vector databases.

Retriever functionality becomes more valuable in future workflows involving:

* Annual Reports
* Investor Presentations
* SEC Filings
* Enterprise Documents

---

## Key Learnings

Day 1:

Multi-Agent Collaboration

Day 2:

Tool Calling + Explainability

Day 3:

LangGraph Workflow Orchestration

Day 4:

Evaluation & Observability

This progression mirrors how production agentic AI systems are typically built and discussed in industry interviews and architecture reviews.
