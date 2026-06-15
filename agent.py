from investment_research_agent.agents.planner_agent import planner_agent
from investment_research_agent.agents.research_agent import research_agent
from investment_research_agent.agents.analyst_agent import analyst_agent
from investment_research_agent.agents.writer_agent import writer_agent

from google.adk.agents import SequentialAgent

root_agent = SequentialAgent(
    name="InvestmentResearchPipeline",
    sub_agents=[
        planner_agent,
        research_agent,
        analyst_agent,
        writer_agent
    ]
)