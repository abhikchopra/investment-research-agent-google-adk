from google.adk.agents import LlmAgent
from investment_research_agent.tools.calculator_tool import calculator_tool

research_agent = LlmAgent(
    name="ResearchAgent",
    model="gemini-2.5-flash",
    tools=[calculator_tool],
    instruction="""
You are an investment researcher.

Use this research plan:

{research_plan}

You may use the calculator tool whenever financial calculations are required.

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