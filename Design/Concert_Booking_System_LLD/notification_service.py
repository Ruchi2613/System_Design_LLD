from user import User
from booking import Booking

class NotificationService:
    def send_confirmation(self, user: User, booking: Booking):
        print("Booking confirmation sent to: " + user.email)
        print("Seats booked:")
        for seat in booking.seats:
            print(seat.seat_number)