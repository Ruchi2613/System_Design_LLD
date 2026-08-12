from car_data_enum import PaymentMethod, PaymentStatus

class Payment:
    def __init__(self, amount: float, method: PaymentMethod):
        self.amount = amount
        self.method = method
        self.status = PaymentStatus.PENDING

    def process_payment(self):
        if self.method == PaymentMethod.CREDIT_CARD:
            self.status = PaymentStatus.SUCCESS

        elif self.method == PaymentMethod.DEBIT_CARD:
            # Simulate debit card processing
            self.status = PaymentStatus.SUCCESS

        elif self.method == PaymentMethod.CASH:
            # Simulate cash payment processing
            self.status = PaymentStatus.SUCCESS

        elif self.method == PaymentMethod.MOBILE_PAYMENT:
            # Simulate mobile payment processing
            self.status = PaymentStatus.SUCCESS
        else:
            self.status = PaymentStatus.FAILED

    
    def get_payment_status(self):
        return self.status