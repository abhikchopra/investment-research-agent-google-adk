from google.adk.agents import LlmAgent

planner_agent = LlmAgent(
    name="PlannerAgent",
    model="gemini-2.5-flash",
    instruction="""
You are an investment research planner.

Create a detailed research plan.

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