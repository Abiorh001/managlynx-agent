# 🧪 CryptoLens Agent Test Suite

Use these queries to test the full range of the agent's new "CFO-Level" capabilities.

## 1. 💰 Portfolio Valuation & Analysis
*Tests: Native Balance, Token Balances, Price Integration, Total Value Calculation*

**Target:** Vitalik Buterin (`0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045`)

1.  "Show me the total portfolio value for `0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045`"
2.  "What are the top 3 token holdings for Vitalik's address?"
3.  "Does this address hold any SHIB?"
4.  "What is the USD value of his ETH balance right now?"

## 2. 🧠 Transaction Intelligence
*Tests: Transaction Fetching, Auto-Categorization (Summarizer), Pattern Recognition*

**Target:** Binance 14 (Active Exchange Wallet) (`0x28C6c06298d514Db089934071355E5743bf21d60`)
*Or random active DeFi user if that one is too noisy.*

1.  "Summarize the last 20 transactions for `0x28C6c06298d514Db089934071355E5743bf21d60`"
2.  "Has this address made any swaps recently?"
3.  "Analyze the gas usage for this wallet over the last 10 transactions"
4.  "Show me the inflow vs outflow for `0x28C6c06298d514Db089934071355E5743bf21d60`"

## 3. 📉 Price & Value Tools (DeFiLlama)
*Tests: Price Fetching, Math, Formatting*

1.  "What is the current price of WETH?" (Contract: `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`)
2.  "How much is 5,000 USDC worth in USD?" (Should be exact)
3.  "Calculate the value of 150 MKR tokens" (MKR: `0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2`)
4.  "What is the price of PEPE?" (PEPE: `0x6982508145454Ce325dDbE47a25d4ec3d2311933`)

## 4. 🕵️‍♂️ Identity & Fund Tracing
*Tests: Metadata, Funding Tracing, Entity Labels*

1.  "Who funded this address: `0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045`?"
2.  "Tell me about this address: `0xe592427a0aece92de3edee1f18e0157c05861564` (Uniswap Router)"
3.  "Is `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48` a contract or a wallet?"

## 5. ⚠️ Error Handling & Edge Cases
*Tests: System Prompt Resilience, Error Catching*

1.  "Analyze address 0x123" (Invalid format)
2.  "What is the price of 0xFakeTokenAddress?" (Non-existent token)
3.  "Show portfolio for `0x0000000000000000000000000000000000000000`" (Burn address - huge balance test)

---

**How to Run:**
```bash
uv run python main.py
```
*Copy and paste any question above!*
