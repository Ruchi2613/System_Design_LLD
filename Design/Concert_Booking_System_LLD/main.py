from user import User
from seat import Seat
from concert import Concert
from booking_system import ConcertBookingSystem


def main():
    # create a concert
    concert = Concert(1, "Coldplay", "Madison Square Garden", "2026-04-01", "7:00 PM")

    # create seats and add them to concert
    seats = []
    for i in range(1, 11):
        seat = Seat(i, f"A{i}", 50)
        concert.add_seat(seat)
        seats.append(seat)  # keep reference to all seat objects

    # create booking system and add concert
    system = ConcertBookingSystem()
    system.add_concert(concert)

    # create users
    user_ruchi = User(1, "Ruchi", "ruchi@email.com", "1234567890")
    user_aditya = User(2, "Aditya", "aditya@email.com", "9876543210")

    # --- Booking for Ruchi ---
    print("\n-- Booking for Ruchi --")
    booking_ruchi = system.book_seats(user_ruchi, concert, ['A1','A2'])
    if booking_ruchi is not None:
        print("Seats booked for Ruchi:")
        for seat in booking_ruchi.seats:
            print(seat.seat_number, "- booked:", seat.is_booked)
        print("Total price:", booking_ruchi.total_price)
    else:
        print("Booking could not be completed for Ruchi.")

    # --- Booking for Aditya ---
    print("\n-- Booking for Aditya --")
    booking_aditya = system.book_seats(user_aditya, concert, ['A3','A4'])
    if booking_aditya is not None:
        print("Seats booked for Aditya:")
        for seat in booking_aditya.seats:
            print(seat.seat_number, "- booked:", seat.is_booked)
        print("Total price:", booking_aditya.total_price)
    else:
        print("Booking could not be completed for Aditya.")

    # show status of all seats
    print("\n-- All seats status --")
    for seat in seats:
        print(seat.seat_number, "- booked:", seat.is_booked)

if __name__ == "__main__":
    main()