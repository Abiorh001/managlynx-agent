# CryptoLens - AI-Powered Ethereum Portfolio Agent

**Talk to your Ethereum wallet with AI** 💼

CryptoLens is an AI-powered portfolio management agent that helps you understand and analyze Ethereum wallets through natural conversation.

## Features

✨ **Natural Language Queries** - Ask questions in plain English  
📊 **CFO-Level Portfolio Tracking** - Real-time balances, prices, and total net worth  
� **Zero-Config Prices** - Integrated **DeFiLlama** (No API keys needed for prices!)  
🔍 **Deep Transaction Analysis** - Auto-summarized activity reports and risk checks  
📡 **Powered by MCP** - Uses Etherscan's Model Context Protocol server  
🤖 **AI-Driven** - GPT-4.1 understands context and financial data  

## Quick Start

```bash
# Install dependencies
uv sync

# Set your LLM API key
export LLM_API_KEY=your_key_here

# Run CryptoLens
uv run python main.py
```

## Example Conversations

**Portfolio Overview:**
```
You: Show portfolio for 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045

CryptoLens: This is Vitalik Buterin's address! 💡
ETH Balance: X.XX ETH
Recent token activity detected...
Would you like me to check specific ERC20 holdings?
```

**Balance Check:**
```
You: What's my USDC balance at 0x...?

CryptoLens: 💰 USDC Balance: 5,432.18 USDC
Would you like to see your USDC transaction history?
```

**Transaction Analysis:**
```
You: Show recent transactions for 0x...

CryptoLens: 📊 Last 7 days:
- 3 outgoing ETH transfers (total 0.5 ETH)
- 2 token swaps detected
- Gas spent: 0.02 ETH
Want to dive into any specific transaction?
```

## Available Queries

### 🏦 Portfolio & Balances
- Show my portfolio for 0x...
- What's the ETH balance for 0x...?
- Check my USDC balance at 0xa0b8...

### 📊 Transactions
- Show recent transactions for 0x...
- Analyze transaction 0x[hash]...
- What happened this week for 0x...?

### 🪙 Token Analysis
- What tokens am I holding at 0x...?
- Tell me about token 0x...
- Am I a top holder of USDC?

### 🔍 Advanced
- Where did my funds come from?
- Get metadata for 0x...
- When was contract 0x... created?

## How It Works

1. **You Ask** - Natural language query about any Ethereum address
2. **AI Plans** - CryptoLens decides which data to fetch
3. **MCP Calls** - Fetches data from Etherscan MCP server (15+ tools)
4. **AI Analyzes** - GPT-4o interprets data and provides insights
5. **You Learn** - Get clear, conversational explanations

## Technology

- **OmniCoreAgent** - Agentic AI framework
- **Etherscan MCP Server** - Blockchain data via Model Context Protocol
- **GPT-4.1** - Advanced language understanding and analysis
- **Python** - Clean, maintainable codebase

## Project Structure

```
 cryptolens/
 ├── main.py                    # Entry point
 ├── cli.py                     # CLI interface
 ├── config.py                  # Configuration loader
 ├── core/
 │   ├── agent.py               # Main agent logic
 │   └── system_prompt.py       # "Master Class" System Instruction
 ├── tools/
 │   ├── mcp_tools.py           # MCP Server config
 │   ├── price_tools.py         # DeFiLlama logic (Consolidated)
 │   └── analysis_tools.py      # Transaction summarization
 └── utils/
     ├── formatting.py          # Value formatting ($1,234.56)
     ├── cache.py               # Smart caching
     └── transaction_analyzer.py # Categorization logic
 ```

## Commands

- `help` - Show query examples
- `exit` - Quit the agent

## Requirements

- Python 3.13+
- OpenAI API key
- Internet connection (for MCP server access)

## Why CryptoLens?

**Traditional Block Explorers:**
- ❌ Complex UI for beginners
- ❌ Data overload
- ❌ No context or insights
- ❌ Requires understanding of blockchain

**CryptoLens:**
- ✅ Conversational AI interface
- ✅ Relevant data only
- ✅ Insights and context
- ✅ Beginner-friendly

## Perfect For

- 📱 Portfolio tracking
- 🔍 Wallet investigation
- 📊 Transaction analysis
- 🎓 Learning about Ethereum
- 🤝 Customer support for blockchain apps

## License

See LICENSE file.

---

**Made with 💙 using OmniCoreAgent**
