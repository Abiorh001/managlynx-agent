"""
CryptoLens - AI-Powered Ethereum Portfolio Agent
"""

import asyncio
from cli import CLI


async def main():
    """Run CryptoLens Portfolio Agent."""
    cli = CLI()
    await cli.initialize()
    await cli.run()


if __name__ == "__main__":
    asyncio.run(main())