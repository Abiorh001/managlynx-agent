"""
Managlynx-Agent Portfolio CLI
"""

from typing import Optional
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text
from core import ManaglynxAgent


class CLI:
    """Clean CLI for Managlynx-Agent portfolio manager."""
    
    def __init__(self):
        """Initialize CLI."""
        self.agent: Optional[ManaglynxAgent] = None
        self.console = Console()
    
    async def initialize(self):
        """Initialize the agent."""
        with self.console.status("[bold green]🚀 Initializing Managlynx-Agent...[/bold green]", spinner="dots"):
            self.agent = ManaglynxAgent()
            await self.agent.initialize()
        self.console.print("[bold green]✅ Agent Ready![/bold green]")
    
    async def run(self):
        """Run the portfolio agent."""
        self._print_welcome()
        
        while True:
            try:
                query = self.console.input("\n[bold cyan]💬 You:[/bold cyan] ").strip()
                
                if not query:
                    continue
                
                # Exit commands
                if query.lower() in ["exit", "quit", "q", "bye"]:
                    self.console.print("\n[bold yellow]👋 Thanks for using Managlynx-Agent![/bold yellow]\n")
                    await self.agent.shutdown()
                    break
                
                # Help command
                if query.lower() in ["help", "h", "?"]:
                    self._print_help()
                    continue
                
                # Process portfolio query
                self.console.print("\n[bold purple]🔍 Analyzing...[/bold purple]")
                
                with self.console.status("[bold blue]Thinking...[/bold blue]", spinner="earth"):
                     result = await self.agent.analyze(query, session_id="session_id")
                
                self.console.print()
                if result:
                    response = result.get("response", "")
                    if not response:
                        self.console.print("[bold red]❌ No response generated.[/bold red]")
                        continue
                    self.console.print(Markdown(response))
                    self.console.print("\n[dim]" + "─" * 70 + "[/dim]")
                else:
                    self.console.print("[bold red]❌ No results found.[/bold red]") 
                
            except KeyboardInterrupt:
                self.console.print("\n\n[bold yellow]👋 Thanks for using Managlynx-Agent![/bold yellow]\n")
                await self.agent.shutdown()
                break
            except Exception as e:
                self.console.print(f"\n[bold red]❌ Error:[/bold red] {str(e)}\n")
                continue
               
    
    def _print_welcome(self):
        """Print welcome message."""
        welcome_text = Text()
        welcome_text.append("\n💼 Managlynx-Agent - Multi-Chain Portfolio Manager", style="bold cyan")
        welcome_text.append("\nTalk to your Ethereum & Solana wallets with AI", style="italic")
        
        self.console.print(Panel(welcome_text, border_style="cyan"))
        
        self.console.print("\n[bold green]💡 Ask me anything about your portfolio![/bold green]")
        self.console.print("\n[bold]📝 Quick Examples:[/bold]")
        self.console.print("   • Show portfolio for [cyan]0xd8dA...[/cyan] (Vitalik)")
        self.console.print("   • Check Solana wallet [cyan]HN7c...[/cyan]")
        self.console.print("   • [yellow]What happened recently?[/yellow]")
        self.console.print("\n[dim]💭 Type 'help' for more examples | 'exit' to quit[/dim]")
        
    def _print_help(self):
        """Print help information."""
        help_md = """
# 📚 CryptoLens Query Examples

### 🏦 Portfolio & Balances
* "Show my portfolio for `0x...`"
* "Check Solana wallet `HN7c...`"
* "How much is my wallet worth?"

### 📊 Transactions
* "Show recent transactions for `0x...`"
* "Analyze my last 10 swaps"
* "Export my transaction history"

### 🪙 Token & NFT Analysis
* "What is the price of SOL?"
* "Tell me about this token"
* "Show my NFT collection"

### 🔍 Advanced
* "Is this contract safe?"
* "Where did my funds come from?"

[dim]Tip: Use full addresses for best results![/dim]
"""
        self.console.print(Panel(Markdown(help_md), title="Help", border_style="blue"))
