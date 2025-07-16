class OrderValidator:
    def __init__(self, order):
        self.order = order

    def validate_order(self):
        return self.order.get('amount', 0) > 0

class OrderSaver:
    def __init__(self, order):
        self.order = order

    def save_to_db(self):
        print(f"Saving order to DB: {self.order}")
    

class OrderManager:
    def __init__(self, order):
        self.order = order
        self.validator = OrderValidator(order)
        self.saver = OrderSaver(order)
    
    def show_confirmation(self):
        print(f"Order confirmed: {self.order}")

    