from abc import ABC, abstractmethod
class TelegramPublisher(ABC):
    @abstractmethod
    def publish(self, post): pass
