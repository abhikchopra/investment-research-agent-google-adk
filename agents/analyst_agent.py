from google.adk.agents import LlmAgent

analyst_agent = LlmAgent(
    name="AnalystAgent",
    model="gemini-2.5-flash",
    instruction="""
Analyze:

{research_notes}

Produce:

Strengths
Weaknesses
Opportunities
Threats
""",
    output_key="investment_analysis"
)