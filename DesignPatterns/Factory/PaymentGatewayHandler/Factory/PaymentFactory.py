from PaymentGateways.PaypalPayment import PaypalPayment
from PaymentGateways.StripePayment import StripePayment
from PaymentGateways.RazorPayment import RazorPayment

class PaymentFactory:
    _creators = {
        'paypal': PaypalPayment,
        'stripe': StripePayment,
        'razorpay': RazorPayment,
    }

    @classmethod
    def create_payment_gateway(cls, gateway_type):
        if gateway_type not in cls._creators:
            raise ValueError(f"Unknown payment gateway type: {gateway_type}")
        return cls._creators[gateway_type]()