"""
Analysis helper tools.
Tools for agent reasoning and analysis workflow.
"""

from typing import TYPE_CHECKING, List, Dict
from utils.transaction_analyzer import TransactionAnalyzer

if TYPE_CHECKING:
    from omnicoreagent import ToolRegistry


def register_analysis_tools(tools: "ToolRegistry") -> None:
    """
    Register analysis helper tools.
    
    Args:
        tools: ToolRegistry instance
    """
    @tools.register_tool(
        name="think",
        description=" reasoned step-by-step analysis for complex queries.",
        inputSchema={
            "type": "object",
            "properties": {
                "thought_process": {
                    "type": "string",
                    "description": "Step-by-step reasoning about the user's request and plan of action."
                }
            },
            "required": ["thought_process"]
        }
    )
    async def think(thought_process: str) -> Dict:
        """
        Structured thinking tool. Returns the thought process as confirmation.
        The agent should use this to plan before taking complex actions.
        """
        return {
            "status": "success",
            "message": "Thinking process confirmed",
            "data": {
                "thought_process": thought_process
            }
        }

    @tools.register_tool(
        name="summarize_transactions",
        description="Analyze a list of transactions to provide a summary of activity (swaps, transfers, gas spent, etc).",
        inputSchema={
            "type": "object",
            "properties": {
                "transactions": {
                    "type": "array",
                    "items": {"type": "object"},
                    "description": "List of transaction objects from Etherscan"
                },
                "address": {
                    "type": "string",
                    "description": "The wallet address being analyzed"
                }
            },
            "required": ["transactions", "address"]
        }
    )
    async def summarize_transactions(transactions: List[Dict], address: str) -> Dict:
        """Analyze transaction patterns."""
        return TransactionAnalyzer.summarize_activity(transactions, address)
