# booking.py
from booking_flight_details import bookingFlight
from payment import Payment

class Booking:
    def __init__(self, user, flight: bookingFlight, seat_no: int, seat_type):
        self.user = user
        self.flight = flight
        self.seat_no = seat_no
        self.seat_type = seat_type
        self.status = "CONFIRMED"

    def confirm_booking(self, amount):
        payment = Payment(amount)
        payment.make_payment()
        if payment.status != "SUCCESS":
            return "Payment failed"

        # 2️⃣ Book seat on flight
        result = self.flight.book_seat(self.seat_type, self.seat_no)
        if "successfully" in result:
            self.status = "CONFIRMED"
            return f"Booking confirmed for seat {self.seat_no} on flight {self.flight.get_flight_name()}"
        else:
            return f"Booking failed: {result}"
        
    def refund(self):
        if self.status == "CANCELLED":
            return "Booking already cancelled"
        
        self.status = "CANCELLED"
        self.flight.cancel_booking(self.seat_no)
        return "Booking Cancelled"