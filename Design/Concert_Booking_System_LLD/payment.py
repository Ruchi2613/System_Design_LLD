class Payment:
    # process payment method
    def process_payment(self, amount):
        # print payment processing message
        print("Processing payment of $" + str(amount) + "...")
        # for simplicity, always return True (payment successful)
        return True