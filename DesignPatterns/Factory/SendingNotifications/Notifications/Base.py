from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass

