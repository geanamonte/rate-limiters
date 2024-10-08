import time
import threading
from rate_limiter.rate_limiter import RateLimiter

class TokenBucketRateLimiter(RateLimiter):
    def __init__(self, rate, capacity):
        """
        Initialize a Token Bucket rate limiter.

        :param rate: Number of tokens added to the bucket per minute (allowed requests per minute).
        :param capacity: Maximum number of tokens the bucket can hold.
        """
        self.rate = rate  # Tokens added per minute
        self.capacity = capacity  # Maximum capacity of the bucket
        self.tokens = capacity  # Current tokens in the bucket
        self.last_checked = time.time()  # Time when tokens were last checked
        self.lock = threading.Lock()  # To make the rate limiter thread-safe

    def _add_tokens(self):
        """
        Refill tokens only when a full minute has passed.
        """
        current_time = time.time()
        elapsed_time = current_time - self.last_checked
        
        if elapsed_time >= 60:
            minutes_passed = int(elapsed_time // 60)
            
            # Add tokens based on the number of full minutes passed
            added_tokens = minutes_passed * self.rate
            self.tokens = min(self.capacity, self.tokens + added_tokens)
            
            # Update the last checked time to the latest minute boundary
            self.last_checked += minutes_passed * 60

    def allow_request(self) -> bool:
        """
        Check if a request is allowed. If there are enough tokens, it consumes one token.
        :return: True if the request is allowed, False otherwise.
        """
        with self.lock:
            self._add_tokens()
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False