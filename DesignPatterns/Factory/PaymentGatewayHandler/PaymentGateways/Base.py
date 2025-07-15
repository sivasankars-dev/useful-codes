from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_pay(self, amount):
        pass

