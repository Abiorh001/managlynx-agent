"""
Simple in-memory cache with TTL support.
"""

import time
from typing import Any, Optional, Dict


class SimpleCache:
    """Time-based cache for API responses."""
    
    def __init__(self, ttl_seconds: int = 300):
        """
        Initialize cache.
        
        Args:
            ttl_seconds: Time-to-live in seconds (default: 5 minutes)
        """
        self.ttl_seconds = ttl_seconds
        self._cache: Dict[str, tuple[Any, float]] = {}
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get cached value if not expired.
        
        Args:
            key: Cache key
            
        Returns:
            Cached value or None if expired/not found
        """
        if key not in self._cache:
            return None
        
        value, timestamp = self._cache[key]
        
        # Check if expired
        if time.time() - timestamp > self.ttl_seconds:
            del self._cache[key]
            return None
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        """
        Cache value with current timestamp.
        
        Args:
            key: Cache key
            value: Value to cache
        """
        self._cache[key] = (value, time.time())
    
    def clear(self) -> None:
        """Clear all cached values."""
        self._cache.clear()
    
    def clear_expired(self) -> None:
        """Remove expired entries."""
        current_time = time.time()
        expired_keys = [
            key for key, (_, timestamp) in self._cache.items()
            if current_time - timestamp > self.ttl_seconds
        ]
        
        for key in expired_keys:
            del self._cache[key]
    
    def size(self) -> int:
        """Get number of cached items."""
        return len(self._cache)
