"""
Formatting utilities for better UX.
Handles address shortening, number formatting, and display helpers.
"""


def shorten_address(address: str) -> str:
    """
    Shorten Ethereum address for display.
    
    Args:
        address: Full Ethereum address (0x + 40 hex chars)
        
    Returns:
        Shortened format: 0xd8dA...6045
        
    Examples:
        >>> shorten_address("0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")
        '0xd8dA...6045'
    """
    if not address or len(address) < 10:
        return address
    
    # Keep first 6 chars (0x + 4 hex) and last 4 chars
    return f"{address[:6]}...{address[-4:]}"


def format_number(value: float, decimals: int = 2) -> str:
    """
    Format number with commas and specified decimals.
    
    Args:
        value: Number to format
        decimals: Number of decimal places (default: 2)
        
    Returns:
        Formatted string with commas
        
    Examples:
        >>> format_number(1234.56)
        '1,234.56'
        >>> format_number(1234567.89, decimals=2)
        '1,234,567.89'
    """
    return f"{value:,.{decimals}f}"


def format_token_amount(amount: float, symbol: str, decimals: int = 4) -> str:
    """
    Format token amount with symbol.
    
    Args:
        amount: Token amount
        symbol: Token symbol (ETH, USDC, etc.)
        decimals: Decimal places (default: 4)
        
    Returns:
        Formatted string: "1,234.5678 ETH"
        
    Examples:
        >>> format_token_amount(1234.5678, "ETH")
        '1,234.5678 ETH'
        >>> format_token_amount(1000, "USDC", decimals=2)
        '1,000.00 USDC'
    """
    formatted_amount = format_number(amount, decimals)
    return f"{formatted_amount} {symbol}"


def format_usd(value: float, decimals: int = 2) -> str:
    """
    Format USD value with dollar sign.
    
    Args:
        value: USD amount
        decimals: Decimal places (default: 2)
        
    Returns:
        Formatted string: "$1,234.56"
        
    Examples:
        >>> format_usd(1234.56)
        '$1,234.56'
        >>> format_usd(1000000)
        '$1,000,000.00'
    """
    formatted = format_number(value, decimals)
    return f"${formatted}"


def format_percentage(value: float, decimals: int = 1) -> str:
    """
    Format percentage value.
    
    Args:
        value: Percentage as decimal (0.45 = 45%)
        decimals: Decimal places (default: 1)
        
    Returns:
        Formatted string: "45.0%"
        
    Examples:
        >>> format_percentage(0.45)
        '45.0%'
        >>> format_percentage(0.1234, decimals=2)
        '12.34%'
    """
    percent = value * 100
    return f"{percent:.{decimals}f}%"


def format_large_number(value: float) -> str:
    """
    Format large numbers with K/M/B suffixes.
    
    Args:
        value: Number to format
        
    Returns:
        Formatted string with suffix
        
    Examples:
        >>> format_large_number(1500)
        '1.5K'
        >>> format_large_number(2500000)
        '2.5M'
        >>> format_large_number(1000000000)
        '1.0B'
    """
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.1f}B"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    elif value >= 1_000:
        return f"{value / 1_000:.1f}K"
    else:
        return f"{value:.1f}"
