import os
from crewai import Agent
from crewai_tools import FileReadTool
from crewai.mcp import MCPServerHTTP, MCPServerSSE
from crewai import LLM
import ssl

from dotenv import load_dotenv
load_dotenv()

# Initialize Gemini LLM with API key from environment
gemini_llm = LLM('gemini-2.5-flash')

SNOWFLAKE_MCP_URL= os.getenv("SNOWFLAKE_MCP_URL")
SNOWFLAKE_PAT_TOKEN= os.getenv("SNOWFLAKE_PAT_TOKEN")

support_agent = Agent(
    role="Customer Support Agent",
    goal="Find and analyze customer support cases and issues reported for a given product",
    backstory=(
        "You are an experienced customer support analyst with expertise in "
        "identifying and categorizing support tickets, customer issues, and "
        "common problems. Your role is to search through support documentation "
        "and identify all relevant cases and issues for a specific product."
    ),
    mcps=[
        MCPServerHTTP(
            url=SNOWFLAKE_MCP_URL,
            headers={"Authorization": f"Bearer {SNOWFLAKE_PAT_TOKEN}"},
            streamable=False,
            cache_tools_list=True
        )],
    tools=[FileReadTool()],
    llm=gemini_llm,
    verbose=True,
)
