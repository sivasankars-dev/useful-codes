from PaymentGateways.Base import PaymentGateway

class RazorPayment(PaymentGateway):
    def process_pay(self, amount):
        return f"Processing payment of ${amount} through Razorpay."


        