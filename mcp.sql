
-- assumption you have already created Cortex Search Service- SUPPORT_CASES. Same works for Cortex Analyst as well.
-- https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp
CREATE OR REPLACE MCP SERVER mcp_server_swt_2025
  FROM SPECIFICATION $$
    tools:
      - name: "SUPPORT_CASE"
        type: "CORTEX_SEARCH_SERVICE_QUERY"
        identifier: "DASH_DB_SWT_2025.RETAIL.SUPPORT_CASES"
        description: "Search support cases using Cortex Search on unstructured support cases data"
        title: "Support Case Search"
  $$;

DESCRIBE MCP SERVER mcp_server_swt_2025;
