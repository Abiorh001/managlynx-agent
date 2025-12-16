"""
CryptoLens Portfolio Agent.
AI-powered portfolio management.
"""

import os
from typing import Optional
from omnicoreagent import OmniAgent, MemoryRouter, EventRouter, ToolRegistry, logger

from .system_prompt import SYSTEM_INSTRUCTION
from tools import register_analysis_tools, register_price_tools
from tools.mcp_tools import MCP_SERVERS


class CryptoLensAgent:
    """AI-powered portfolio management"""
    
    def __init__(self):
        """
        Initialize the CryptoLens portfolio agent.
        """
        self.tools: Optional[ToolRegistry] = None
        self.agent: Optional[OmniAgent] = None
        self.memory_router: Optional[MemoryRouter] = None
        self.event_router: Optional[EventRouter] = None
        self.mcp_servers_connected: bool = False
    
    def _create_tools(self) -> ToolRegistry:
        """
        Create and register local tools.
        
        Note: Contract interaction tools for Ethereum are provided by MCP server.
        Local tools are for analysis helpers and price lookups.
        
        Returns:
            Configured ToolRegistry
        """
        tools = ToolRegistry()
        
        # Register analysis helper tools
        register_analysis_tools(tools)
        
        # Register price tools
        register_price_tools(tools)
        
        local_tool_count = len(tools.list_tools())
        if local_tool_count > 0:
            logger.info(f"✅ Registered {local_tool_count} local tool(s)")
        
        return tools
    
    async def initialize(self):
        """Initialize the agent and all components."""
        logger.info("🚀 Initializing CryptoLens Portfolio Agent...")
        
        # Create routers uncomment if you have redis or checkout the documentation
        # self.memory_router = MemoryRouter("redis")
        # self.event_router = EventRouter("redis_stream")
        
        # Create and register tools
        self.tools = self._create_tools()
        
        # Create the agent
        self.agent = OmniAgent(
            name="cryptolens_portfolio",
            system_instruction=SYSTEM_INSTRUCTION,
            model_config={
                "provider": "openai",
                "model": "gpt-4.1",
                "temperature": 0.1,
                "max_context_length": 128000,
            },
            local_tools=self.tools,
            mcp_tools=MCP_SERVERS,
            agent_config={
                "max_steps": 20,
                "tool_call_timeout": 60,
                "memory_config": {"mode": "token_budget", "value": 20000},
            },
            # memory_router=self.memory_router,
            # event_router=self.event_router,
            debug=True
        )
        await self.agent.connect_mcp_servers()
        self.mcp_servers_connected = True
        
        logger.info("✅ CryptoLens initialized successfully")
       
    
    async def analyze(self, query: str, session_id: str = None) -> str:
        """
        Analyze a smart contract based on user query.
        
        Args:
            query: User query (e.g., "Analyze 0x... on ethereum")
            
        Returns:
            Analysis result as formatted text
            
        Raises:
            RuntimeError: If agent not initialized
        """
        if not self.agent:
            raise RuntimeError("Agent not initialized. Call initialize() first.")
        
        try:
            result = await self.agent.run(query=query, session_id=session_id)
            return result
        except ValueError as e:
            # Handle specific validation errors
            return f"❌ Input Error: {str(e)}\nInput should be a valid Ethereum address (0x...)."
        except Exception as e:
            # Generic catch-all with user-friendly message
            logger.error(f"❌ Analysis failed: {str(e)}")
            return f"❌ Something went wrong: {str(e)}\n\n💡 Tip: Try checking the address or rephrasing your query."

    async def shutdown(self):
        """Shutdown the agent and all components."""
        if self.agent:
            print("Shutting down CryptoLens agent...")
            await self.agent.cleanup()