from PaymentGateways.Base import PaymentGateway

class StripePayment(PaymentGateway):
    def process_pay(self, amount):
        return f"Processing payment of ${amount} through Stripe."
