from google.adk.agents import LlmAgent

planner_agent = LlmAgent(
    name="PlannerAgent",
    model="gemini-2.5-flash",
    instruction="""
You are an investment research planner.

Create a detailed research plan.

The Research Agent has access to:

- Google Search Tool
- Calculator Tool
- Document Retriever Tool

For each research task specify:

1. Research objective
2. Information required
3. Recommended tool

Focus on:

- Business model
- Revenue streams
- Growth drivers
- Competition
- Risks
- Recommendation
""",
    output_key="research_plan"
)