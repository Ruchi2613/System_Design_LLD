# main.py

from aircraft_crew_details import Aircraft, Crew
from airline_search import AirlineSystem
from booking_flight_details import bookingFlight
from seat import seat
from seat_enum import seatTypes, seatAvailableStatus
from user_details import user_details
from way_enum import Way
from user_role import UserRole
from booking_refund import Booking
from payment import Payment

# ----------------------------
# Create Aircraft and Crew
# ----------------------------
aircraft1 = Aircraft(aircraft_id=1, model="Boeing 737")
crew1 = Crew(crew_id=101, name="John Smith", role="Pilot")
crew2 = Crew(crew_id=102, name="Alice Brown", role="Cabin Crew")

print(f"Aircraft: {aircraft1.model}, Crew: {crew1.name}, {crew2.name}")

# ----------------------------
# Create Seats for Flight
# ----------------------------
seats = []
for i in range(1, 11):
    # Alternate seat types for variety
    if i <= 4:
        seat_type = seatTypes.SMALL
    elif i <= 7:
        seat_type = seatTypes.MEDIUM
    else:
        seat_type = seatTypes.LARGE
    s = seat(seat_id=i, seat_no=i, seat_type=seat_type)
    seats.append(s)

# ----------------------------
#  Create Flights
# ----------------------------
flight1 = bookingFlight(
    flight_name="Indigo",
    flight_num="6E123",
    source="Delhi",
    destination="Mumbai",
    departure_time="10:00",
    arrival_time="12:00",
    available_seats=seats
)

flight2 = bookingFlight(
    flight_name="Air India",
    flight_num="AI456",
    source="Delhi",
    destination="Mumbai",
    departure_time="15:00",
    arrival_time="17:30",
    available_seats=seats.copy()
)

# ----------------------------
# Create Airline System and Add Flights
# ----------------------------
airline_system = AirlineSystem()
airline_system.add_flight(flight1)
airline_system.add_flight(flight2)

# ----------------------------
# Search for Flights
# ----------------------------
print("\nSearching flights from Delhi to Mumbai...")
available_flights = airline_system.search_flight("Delhi", "Mumbai")
for f in available_flights:
    print(f"Flight: {f.get_flight_name()}, Number: {f.get_flight_num()}, Departure: {f.get_departure_time()}")

# ----------------------------
# Create User
# ----------------------------
user1 = user_details(
    u_name="Ruchi Pandey",
    u_id=1,
    u_add="Beaux Arts Village",
    u_flight_name=flight1.get_flight_name(),
    u_mail_id="ruchi@example.com",
    u_destination="Mumbai",
    booking_date="2026-03-18",
    u_way=Way.ONE_WAY,
    u_seat_booking_count=1
)

print("\nUser Details:")
print(user1.get_user_details())

# ----------------------------
# Book a Seat
# ----------------------------
seat_to_book = 3
seat_type_to_book = seatTypes.MEDIUM
amount = 5000

booking1 = Booking(user=user1, flight=flight1, seat_no=seat_to_book, seat_type=seat_type_to_book)
booking_result = booking1.confirm_booking(amount)

print("\nBooking Result:")
print(booking_result)

# ----------------------------
# Show Available Seats After Booking
# ----------------------------
print("\nAvailable Seats after booking:")
available_seats_after = flight1.get_available_seats()
for s in available_seats_after:
    print(f"Seat No: {s.seat_no}, Type: {s.seat_type.value}, Status: {s.seat_status.value}")

# ----------------------------
# Cancel Booking
# ----------------------------
print("\nCancelling Booking...")
refund_result = booking1.refund()
print(refund_result)

# ----------------------------
# Show Available Seats After Cancellation
# ----------------------------
print("\nAvailable Seats after cancellation:")
available_seats_final = flight1.get_available_seats()
for s in available_seats_final:
    print(f"Seat No: {s.seat_no}, Type: {s.seat_type.value}, Status: {s.seat_status.value}")