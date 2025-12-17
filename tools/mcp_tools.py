MCP_SERVERS = [
    {
        "name": "etherscan-server",
        "url": "https://mcp.etherscan.io/mcp",
        "transport_type": "streamable_http",
        "headers": {
            "Authorization": "Bearer your_etherscan_api_key_here"
        }
    },
    {
        "name": "evm-mcp-server",
        "command": "npx",
        "args": ["-y", "@mcpdotdirect/evm-mcp-server"]
    },
    {
        "name": "solscan-mcp",
        "command": "/home/abiorh/.cargo/bin/solscan-mcp",
        "args": [],
        "env": {
        "SOLSCAN_API_KEY": "your_solscan_api_key_here"
      }

    }
]