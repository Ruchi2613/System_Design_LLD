from coffe_type_enum import PaymentMethod, PaymentStatus

class Payment:
    def __init__(self, amount: float, method: PaymentMethod):
        self.amount = amount
        self.method = method
        self.status = PaymentStatus.PENDING

    def process_payment(self):
        if self.method == PaymentMethod.CASH:
            print(f"Processing cash payment of ${self.amount:.2f}...")
            self.status = PaymentStatus.COMPLETED

        elif self.method == PaymentMethod.CARD:
            print(f"Processing card payment of ${self.amount:.2f}...")
            self.status = PaymentStatus.COMPLETED
        elif self.method == PaymentMethod.MOBILE_PAYMENT:
            print(f"Processing mobile payment of ${self.amount:.2f}...")
            self.status = PaymentStatus.COMPLETED
        else:
            print("Invalid payment method.")
            self.status = PaymentStatus.FAILED

    def get_status(self):
        return self.status