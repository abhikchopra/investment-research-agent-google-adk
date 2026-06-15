from google.adk.agents import LlmAgent

writer_agent = LlmAgent(
    name="WriterAgent",
    model="gemini-2.5-flash",
    instruction="""
Create a professional investment report.

Use:

{investment_analysis}

Include:

Executive Summary
Business Overview
Bull Case
Bear Case
Risks
Recommendation
""",
    output_key="final_report"
)