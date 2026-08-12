class Seat:
    def __init__(self, seat_id, seat_number, price):
        # unique id of the seat
        self.seat_id = seat_id
        # seat number like A1, A2
        self.seat_number = seat_number
        # price of the seat
        self.price = price
        # flag to check if seat is booked
        self.is_booked = False

    # method to book the seat
    def book(self):
        if self.is_booked == True:
            # seat already booked, cannot book again
            return False
        # mark the seat as booked
        self.is_booked = True
        return True

    # method to release the seat if payment fails
    def release(self):
        # mark seat as available again
        self.is_booked = False
