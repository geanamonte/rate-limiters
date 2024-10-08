from abc import ABC
from abc import abstractmethod

class RateLimiter(ABC):
    @abstractmethod
    def allow_request(self) -> bool:
        pass