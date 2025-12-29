"""
Security middleware for production-grade API
"""
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import re
from typing import Any, Dict

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Add security headers to all responses"""
    
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
        
        # Content Security Policy
        csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval'; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' https: data:; "
            "connect-src 'self'; "
            "frame-ancestors 'none';"
        )
        response.headers["Content-Security-Policy"] = csp
        
        return response


def validate_string_input(value: str, max_length: int = 500, field_name: str = "field") -> str:
    """Validate and sanitize string inputs"""
    if not value:
        raise HTTPException(status_code=400, detail=f"{field_name} cannot be empty")
    
    # Remove any potential script tags or malicious content
    cleaned_value = re.sub(r'<script[^>]*>.*?</script>', '', value, flags=re.IGNORECASE | re.DOTALL)
    cleaned_value = cleaned_value.strip()
    
    if len(cleaned_value) > max_length:
        raise HTTPException(
            status_code=400, 
            detail=f"{field_name} exceeds maximum length of {max_length} characters"
        )
    
    return cleaned_value


def validate_price(price: str) -> str:
    """Validate price format"""
    if not re.match(r'^\d+\.?\d{0,2}$', price):
        raise HTTPException(status_code=400, detail="Invalid price format")
    
    price_float = float(price)
    if price_float < 0 or price_float > 999.99:
        raise HTTPException(status_code=400, detail="Price must be between 0 and 999.99")
    
    return price


def validate_url(url: str) -> str:
    """Validate URL format"""
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )
    
    if not url_pattern.match(url):
        raise HTTPException(status_code=400, detail="Invalid URL format")
    
    return url


class RateLimitInfo:
    """Simple in-memory rate limiting info"""
    def __init__(self):
        self.requests: Dict[str, list] = {}
    
    def check_rate_limit(self, client_ip: str, max_requests: int = 100, window_seconds: int = 60) -> bool:
        """Check if client has exceeded rate limit"""
        import time
        current_time = time.time()
        
        if client_ip not in self.requests:
            self.requests[client_ip] = []
        
        # Remove old requests outside the window
        self.requests[client_ip] = [
            req_time for req_time in self.requests[client_ip]
            if current_time - req_time < window_seconds
        ]
        
        # Check if limit exceeded
        if len(self.requests[client_ip]) >= max_requests:
            return False
        
        # Add current request
        self.requests[client_ip].append(current_time)
        return True


# Global rate limiter instance
rate_limiter = RateLimitInfo()
