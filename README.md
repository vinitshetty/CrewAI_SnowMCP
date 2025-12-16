# CrewAI (Agentic AI) + Snowflake MCP Integration

Simple project demonstrating how to integrate CrewAI agents with Snowflake via MCP (Model Context Protocol) to expose Snowflake resources and tools to AI agents.

---

## 🚀 TLDR - Just 2 Lines of Code

Add an MCP server to any CrewAI Agent definition:

```python
support_agent = Agent(
    role="Customer Support Agent",
    goal="Analyze customer support cases",
    # ... other config ...
    mcps=[
        MCPServerHTTP(
            url=SNOWFLAKE_MCP_URL,
            headers={"Authorization": f"Bearer {SNOWFLAKE_PAT_TOKEN}"},
        )
    ],
)
```

That's it. Your agent now has access to all Snowflake MCP tools and resources.

---

## Setup

### 1. Environment Variables

```.env file
SNOWFLAKE_PAT_TOKEN=your_pat_token
SNOWFLAKE_MCP_URL=your_mcp_server_url
GOOGLE_API_KEY=your_gemini_key
```

**MCP URL Format:**
```
https://<org>-<account>.snowflakecomputing.com/api/v2/databases/<DATABASE>/schemas/<SCHEMA>/mcp-servers/<MCP_SERVER_NAME>
```

Example:
```
https://sfsenorthamerica-sg_demo13.snowflakecomputing.com/api/v2/databases/DASH_DB_SWT_2025/schemas/RETAIL/mcp-servers/mcp_server_swt_2025
```

### 2. Install & Run

```bash
uv sync
python main.py
```

## How It Works

1. **Snowflake MCP Server** exposes tools (Cortex Search, Cortex Analyst, etc.)
2. **CrewAI Agent** connects via `MCPServerHTTP` 
3. **Agent automatically discovers** available tools and uses them to complete tasks

## Troubleshooting

> **SSL Certificate Issues?** If you encounter certificate errors during testing, set `verify=False` in `.venv/lib/python3.13/site-packages/mcp/shared/_httpx_utils.py` (line 83). *For testing only—not recommended for production.*

I have logged issue here - https://github.com/crewAIInc/crewAI/issues/4100

## Resources

- [Snowflake MCP Documentation](https://docs.snowflake.com/en/developer-guide/mcp/overview)
- [CrewAI MCP Integration](https://docs.crewai.com/concepts/mcp)
