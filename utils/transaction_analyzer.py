"""
Transaction analysis and categorization utilities.
Helps identify transaction types (Swap, Transfer, DeFi) and calculate net changes.
"""

from typing import Dict, List, Optional
from datetime import datetime

class TransactionAnalyzer:
    """Analyze transaction patterns and categorize activity."""
    
    @staticmethod
    def categorize_transaction(tx: Dict) -> str:
        """
        Determine transaction type based on patterns.
        
        Args:
            tx: Transaction dictionary from Etherscan
            
        Returns:
            Type string: 'Swap', 'Transfer', 'Approve', 'DeFi Deposit', etc.
        """
        # 1. Check method ID if available
        method_id = tx.get("methodId", "").lower()
        if method_id:
            # Common method IDs
            if method_id.startswith("0xa9059cbb"): return "Transfer (ERC20)"
            if method_id.startswith("0x095ea7b3"): return "Approve"
            if method_id.startswith("0x23b872dd"): return "TransferFrom"
            
            # Uniswap / DEX patterns
            if method_id in ["0x7ff36ab5", "0x38ed1739", "0x18cbafe5", "0xfb3bdb41"]:
                return "Swap"
                
            # Deposit/Withdraw patterns (generic)
            if method_id.startswith("0xd0e30db0"): return "Deposit"
            if method_id.startswith("0x2e1a7d4d"): return "Withdraw"

        # 2. Check value and input
        has_value = int(tx.get("value", "0")) > 0
        has_input = len(tx.get("input", "0x")) > 2
        
        if has_value and not has_input:
            return "ETH Transfer"
            
        if not has_value and has_input:
            return "Contract Interaction"
            
        return "Transaction"

    @staticmethod
    def summarize_activity(transactions: List[Dict], address: str) -> Dict:
        """
        Summarize a list of transactions.
        
        Args:
            transactions: List of transaction objects
            address: The user's wallet address (case insensitive)
            
        Returns:
            Summary dict with counts and key stats
        """
        addr_lower = address.lower()
        summary = {
            "total_count": len(transactions),
            "swaps": 0,
            "transfers_in": 0,
            "transfers_out": 0,
            "approvals": 0,
            "interactions": 0,
            "volume_eth_in": 0.0,
            "volume_eth_out": 0.0,
            "gas_spent": 0.0
        }
        
        for tx in transactions:
            # Stats
            value_eth = float(tx.get("value", 0)) / 1e18
            gas_eth = (float(tx.get("gasUsed", 0)) * float(tx.get("gasPrice", 0))) / 1e18
            summary["gas_spent"] += gas_eth
            
            # Direction
            is_outgoing = tx.get("from", "").lower() == addr_lower
            
            if is_outgoing:
                summary["volume_eth_out"] += value_eth
            else:
                summary["volume_eth_in"] += value_eth

            # Categorize
            category = TransactionAnalyzer.categorize_transaction(tx)
            
            if category == "Swap":
                summary["swaps"] += 1
            elif "Transfer" in category or category == "ETH Transfer":
                if is_outgoing:
                    summary["transfers_out"] += 1
                else:
                    summary["transfers_in"] += 1
            elif category == "Approve":
                summary["approvals"] += 1
            else:
                summary["interactions"] += 1
                
        return {
            "status": "success",
            "data": summary
        }
