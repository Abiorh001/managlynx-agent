"""
Tools package.
Provides tool registration for the smart contract analysis agent.

Note: Contract interaction tools (source code, ABI, bytecode) are provided
by the Etherscan MCP server. Local tools are only for analysis helpers and prices.
"""

from tools.analysis_tools import register_analysis_tools
from tools.price_tools import register_price_tools

__all__ = [
    "register_analysis_tools",
    "register_price_tools",
]
