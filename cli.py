"""
CryptoLens Portfolio Agent CLI
"""

from typing import Optional
from core import CryptoLensAgent


class CLI:
    """Clean CLI for CryptoLens portfolio agent."""
    
    def __init__(self):
        """Initialize CLI."""
        self.agent: Optional[CryptoLensAgent] = None
    
    async def initialize(self):
        """Initialize the agent."""
        self.agent = CryptoLensAgent()
        await self.agent.initialize()
    
    async def run(self):
        """Run the portfolio agent."""
        self._print_welcome()
        
        while True:
            try:
                query = input("\n💬 You: ").strip()
                
                if not query:
                    continue
                
                # Exit commands
                if query.lower() in ["exit", "quit", "q", "bye"]:
                    print("\n👋 Thanks for using CryptoLens!\n")
                    await self.agent.shutdown()
                    break
                
                # Help command
                if query.lower() in ["help", "h", "?"]:
                    self._print_help()
                    continue
                
                # Process portfolio query
                print("\n🔍 Analyzing...\n")
                result = await self.agent.analyze(query, session_id="session_id")
                print(f"\n{result}\n")
                print("─" * 70)
                
            except KeyboardInterrupt:
                print("\n\n👋 Thanks for using CryptoLens!\n")
                await self.agent.shutdown()
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}\n")
                await self.agent.shutdown()
    
    def _print_welcome(self):
        """Print welcome message."""
        print("\n" + "═" * 70)
        print("  💼 CryptoLens - AI-Powered Ethereum Portfolio Agent")
        print("═" * 70)
        print("\n💡 Ask me anything about Ethereum wallets and portfolios!")
        print("\n📝 Quick Examples:")
        print("   • Show portfolio for 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")
        print("   • What's my ETH balance for 0x...")
        print("   • Analyze recent transactions for 0x...")
        print("   • Check USDC holdings at 0x...")
        print("\n💭 Type 'help' for more examples | 'exit' to quit")
        print("═" * 70)
    
    def _print_help(self):
        """Print help information."""
        print("\n" + "─" * 70)
        print("📚 CryptoLens Query Examples")
        print("─" * 70)
        
        print("\n🏦 Portfolio & Balances:")
        print("   • Show my portfolio for 0x...")
        print("   • What's the ETH balance for 0x...")
        print("   • Check my USDC balance at 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")
        print("   • How much WETH do I have?")
        
        print("\n📊 Transactions:")
        print("   • Show recent transactions for 0x...")
        print("   • Analyze transaction 0x[hash]...")
        print("   • What transactions happened this week for 0x...")
        print("   • Show me all token transfers for 0x...")
        
        print("\n🪙 Token Analysis:")
        print("   • What tokens am I holding at 0x...")
        print("   • Tell me about token 0x... (contract address)")
        print("   • Am I a top holder of USDC?")
        print("   • Show ERC20 transfers for 0x...")
        
        print("\n🔍 Advanced:")
        print("   • Where did my funds come from? (for address 0x...)")
        print("   • Get metadata for address 0x...")
        print("   • When was contract 0x... created?")
        print("   • Show me the contract source for 0x...")
        
        print("\n💡 Tips:")
        print("   • Use full addresses (0x + 40 characters)")
        print("   • Transaction hashes are 0x + 64 characters")
        print("   • Be specific about which address you're asking about")
        
        print("─" * 70)
