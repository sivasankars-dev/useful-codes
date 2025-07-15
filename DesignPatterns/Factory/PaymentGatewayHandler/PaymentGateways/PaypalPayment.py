from PaymentGateways.Base import PaymentGateway

class PaypalPayment(PaymentGateway):
    def process_pay(self, amount):
        return f"Processing payment of ${amount} through PayPal."
        