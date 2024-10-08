import unittest
import time
from rate_limiter.token_bucket import TokenBucketRateLimiter


class TestTokenBucket(unittest.TestCase):
    def test_10_requests_no_interval(self):
        limiter = TokenBucketRateLimiter(rate=4, capacity=4)
        result = [True] * 4 + [False] * 6
        to_check = []
        for i in range(10):
            to_check.append(limiter.allow_request())
            if to_check[i]:
                print(f"Request {i} is allowed.")
            else:
                print(f"Request {i} is rate-limited. Waiting for more tokens.")
            time.sleep(0.2)
        self.assertEqual(result, to_check)

    def test_10_requests_10s_interval(self):
        limiter = TokenBucketRateLimiter(rate=4, capacity=4)
        result = [True] * 4 + [False] * 2 + [True] * 4
        to_check = []
        for i in range(10):
            to_check.append(limiter.allow_request())
            time.sleep(10)
            if to_check[i]:
                print(f"Request {i} is allowed.")
            else:
                print(f"Request {i} is rate-limited. Waiting for more tokens.")
        self.assertEqual(result, to_check)