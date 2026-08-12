class Payment:
    def __init__(self, amount):
        self.amount = amount
        self.status = "PENDING"

    def make_payment(self):
        self.status = "SUCCESS"
        return "Payment Successful"