from Factory.PaymentFactory import PaymentFactory

if __name__ == "__main__":
    for gateway in ["paypal", "stripe", "razorpay"]:
        handler = PaymentFactory.create_payment_gateway(gateway)
        print(handler.process_pay(100))