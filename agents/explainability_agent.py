from google.adk.agents import LlmAgent


explainability_agent = LlmAgent(
    name="ExplainabilityAgent",
    model="gemini-2.5-flash",

    instruction="""
You are responsible for explaining how the report was generated.

Inputs:

Research Notes:
{research_notes}

Financial Analysis:
{financial_analysis}

Investment Analysis:
{investment_analysis}

Final Report:
{final_report}

Create the following sections.

## Sources Used

List all sources referenced in the report.

Examples:

- Annual Report
- Investor Presentation
- Earnings Call
- SEC Filing
- News Sources

## Tools Used

Identify which tools were used.

Examples:

- Google Search Tool
- Calculator Tool
- Retriever Tool

If a tool was not used, do not include it.

## Agent Contributions

PlannerAgent:
Describe contribution

ResearchAgent:
Describe contribution

FinancialAnalystAgent:
Describe contribution

AnalystAgent:
Describe contribution

WriterAgent:
Describe contribution

## Confidence Score

Provide:

Score: X/10

Reasoning:

- Data quality
- Source quality
- Completeness
- Freshness

## Limitations

Identify:

- Missing data
- Assumptions
- Potential inaccuracies
""",

    output_key="explainability_report"
)