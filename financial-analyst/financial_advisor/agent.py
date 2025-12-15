from google.genai import types
from google.adk.tools import ToolContext
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.models.lite_llm import LiteLlm
from .sub_agents.data_analyst import data_analyst
from .sub_agents.financial_analyst import financial_analyst
from .sub_agents.new_analyst import news_analyst
from .prompt import PROMPT

MODEL = LiteLlm(model="gpt-4o")


async def save_advice_report(tool_context: ToolContext, summary: str, ticker: str):
    state = tool_context.state
    data_analyst_result = state.get("data_analyst_result")
    financial_analyst_result = state.get("financial_analyst_result")
    news_analyst_result = state.get("news_analyst_result")
    report = f"""
        # Summary
        {summary}
        
        ## Data Analyst Result
        {data_analyst_result}
        
        ## Financial Analyst Result
        {financial_analyst_result}
        
        ## News Analyst Result
        {news_analyst_result}
    """
    state["report"] = report

    filename = f"{ticker}_investment_advice.md"
    
    artifact = types.Part(
        inline_data=types.Blob(
            mime_type="text/markdown",
            data=report.encode("utf-8"),
        )
    )

    await tool_context.save_artifact(filename, artifact)
    
    return {
        "success": True,
    }


financial_advisor_agent = Agent(
    name="financial_advisor_agent",
    instruction=PROMPT,
    model=MODEL,
    tools=[
        save_advice_report,
        AgentTool(data_analyst),
        AgentTool(financial_analyst),
        AgentTool(news_analyst),
    ],
)

root_agent = financial_advisor_agent
