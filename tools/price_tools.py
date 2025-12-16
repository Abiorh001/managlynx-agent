"""
CoinGecko price integration tools.
Provides real-time token prices and portfolio valuation.
"""

import aiohttp
from typing import Dict, List, Optional, TYPE_CHECKING
from omnicoreagent import logger

if TYPE_CHECKING:
    from omnicoreagent import ToolRegistry

from utils.cache import SimpleCache
from utils.formatting import format_usd


class PriceService:
    """DeFiLlama API integration for token prices (Free & Keyless)."""
    
    # DeFiLlama Coins API endpoint
    BASE_URL = "https://coins.llama.fi/prices/current"
    
    def __init__(self):
        """Initialize price service with cache."""
        # Cache prices for 5 minutes
        self.cache = SimpleCache(ttl_seconds=300)
    
    async def get_token_price(self, contract_address: str) -> Optional[Dict]:
        """
        Get token price from DeFiLlama.
        
        Args:
            contract_address: Ethereum contract address or 'eth'
            
        Returns:
            Dict with price data or None if not found
        """
        if not contract_address:
            return None

        # Normalize address
        address_lower = contract_address.lower()
        
        # Check cache
        cache_key = f"price:{address_lower}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached
        
        try:
            # Determine DeFiLlama query ID
            # Native ETH
            if address_lower in ["0x0000000000000000000000000000000000000000", "eth"]:
                query_id = "coingecko:ethereum"
            # ERC20 Token
            else:
                query_id = f"ethereum:{address_lower}"
            
            # Fetch from API
            price_data = await self._fetch_price(query_id)
            
            # Cache result if found
            if price_data:
                self.cache.set(cache_key, price_data)
            
            return price_data
            
        except Exception as e:
            logger.error(f"Error fetching price for {contract_address}: {str(e)}")
            return None
    
    async def _fetch_price(self, query_id: str) -> Optional[Dict]:
        """Fetch price from DeFiLlama."""
        url = f"{self.BASE_URL}/{query_id}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    # DeFiLlama returns {"coins": {"ethereum:0x...": {"price": ...}}}
                    coins = data.get("coins", {})
                    if query_id in coins:
                        item = coins[query_id]
                        return {
                            "usd": item.get("price"),
                            # DeFiLlama doesn't always provide 24h change in this endpoint, 
                            # but simpler implementation is preferred for MVP.
                            # We'll map what we have.
                            "usd_market_cap": None  # Not provided by this endpoint
                        }
        return None
    
    async def calculate_token_value(
        self, 
        amount: float, 
        contract_address: str
    ) -> Optional[float]:
        """Calculate USD value of token amount."""
        try:
            price_data = await self.get_token_price(contract_address)
            if not price_data or "usd" not in price_data:
                return None
                
            price = float(price_data["usd"])
            return amount * price
        except Exception:
            return None

# Global price service instance
_price_service = None

def get_price_service() -> PriceService:
    """Get global price service instance."""
    global _price_service
    if _price_service is None:
        _price_service = PriceService()
    return _price_service


def register_price_tools(tools: "ToolRegistry") -> None:
    """
    Register price-related tools with the agent.
    
    Args:
        tools: ToolRegistry instance
    """
    price_service = get_price_service()
    
    @tools.register_tool(
        name="get_token_price",
        description="Get USD price and calculate value for a token. Input balance to get total value.",
        inputSchema={
            "type": "object",
            "properties": {
                "contract_address": {
                    "type": "string",
                    "description": "Token contract address (0x...) or 'eth'"
                },
                "balance": {
                    "type": "number",
                    "description": "Optional: Amount of tokens to calculate total USD value"
                }
            },
            "required": ["contract_address"]
        }
    )
    async def get_token_price_tool(contract_address: str, balance: float = None) -> dict:
        """Get price and optionally calculate value."""
        price_data = await price_service.get_token_price(contract_address)
        
        if not price_data:
            return {
                "status": "error",
                "error": f"Price not found for {contract_address}"
            }
        
        price = price_data.get("usd", 0)
        
        response = {
            "status": "success",
            "message": "Price fetched successfully",
            "data": {
                "contract_address": contract_address,
                "usd_price": price,
                "formatted_price": format_usd(price)
            }
        }

        # If balance provided, calculate total value
        if balance is not None:
            value = price * balance
            response["data"]["balance_amount"] = balance
            response["data"]["total_value_usd"] = value
            response["data"]["formatted_value"] = format_usd(value)
        
        return response
