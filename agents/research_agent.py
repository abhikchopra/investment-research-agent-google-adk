from google.adk.agents import LlmAgent

research_agent = LlmAgent(
    name="ResearchAgent",
    model="gemini-2.5-flash",
    instruction="""
You are an investment researcher.

Use this research plan:

{research_plan}

Produce structured research notes covering:

- Business Overview
- Revenue Streams
- AI Strategy
- Competitive Position
- Financial Position
- Risks
""",
    output_key="research_notes"
)