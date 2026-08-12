from booking import Booking
from payment import Payment
from notification_service import NotificationService

class ConcertBookingSystem:
    def __init__(self):
        self.concerts = []
        self.bookings = []

    def add_concert(self, concert):
        self.concerts.append(concert)

    def search_concert(self, artist=None, venue=None):
        results = []
        for concert in self.concerts:
            if artist != None and artist.lower() not in concert.artist.lower():
                continue
            if venue != None and venue.lower() not in concert.venue.lower():
                continue
            results.append(concert)
        return results

    def book_seats(self, user, concert, seat_numbers):
        selected_seats = []
        for seat in concert.seats:
            for num in seat_numbers:
                if seat.seat_number == num:
                    success = seat.book()
                    if not success:
                        print("Seat already booked: " + seat.seat_number)
                        return None
                    selected_seats.append(seat)
        booking = Booking(len(self.bookings)+1, user, concert, selected_seats)
        payment = Payment()
        if payment.process_payment(booking.total_price):
            booking.confirm()
            self.bookings.append(booking)
            notifier = NotificationService()
            notifier.send_confirmation(user, booking)
            return booking
        else:
            for seat in selected_seats:
                seat.release()
            return None