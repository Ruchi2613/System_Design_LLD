from typing import List
from seat import Seat
from user import User
from concert import Concert

class Booking:
    def __init__(self, booking_id, user: User, concert: Concert, seats):
        # unique id for booking
        self.booking_id = booking_id
        # user who booked
        self.user = user
        # concert booked
        self.concert = concert
        # seats booked
        self.seats: List[Seat] = []
        # calculate total price by summing price of each seat
        total = 0
        for seat in seats:
            total += seat.price
        self.total_price = total
        # initial status is pending
        self.status = "PENDING"

    # method to confirm booking
    def confirm(self):
        # set status to confirmed
        self.status = "CONFIRMED"