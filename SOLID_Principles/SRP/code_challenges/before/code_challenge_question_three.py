# 3. OrderProcessor – Business + UI + Storage
class OrderProcessor:
    def __init__(self, order):
        self.order = order

    def validate_order(self):
        return self.order.get('amount', 0) > 0

    def save_to_db(self):
        print(f"Saving order to DB: {self.order}")

    def show_confirmation(self):
        print(f"Order confirmed: {self.order}")
