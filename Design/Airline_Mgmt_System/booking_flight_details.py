from seat_enum import seatTypes, seatAvailableStatus
from user_details import user_details
from typing import List
from seat import seat
from payment import Payment


class bookingFlight:
    def __init__(self, flight_name, flight_num, source, destination, departure_time, arrival_time, available_seats):
        self.flight_name = flight_name
        self.flight_num = flight_num
        self.source = source
        self.destination = destination 
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.available_seats = available_seats


    def get_flight_name(self):
        return self.flight_name
    
    def get_flight_num(self):
        return self.flight_num

    def get_source(self):
        return self.source
    
    def get_departure_time(self):
        return self.departure_time
    
    def get_arrival_time(self):
        return self.arrival_time
    
    def get_available_seats(self):
        available = []
        for s in self.available_seats:
            if s.seat_status == seatAvailableStatus.AVAILABLE:
                available.append(s)
        return available
    

    def book_seat(self ,seat_type: seatTypes, seat_no: int):
        
        for s in self.available_seats:

            
            if s.seat_no == seat_no:
                # Step 2: check seat type
                if s.seat_type != seat_type:
                    return f"Seat {seat_no} is not of type {seat_type.value}"
                
                if s.seat_status != seatAvailableStatus.AVAILABLE:
                    return f"Seat {seat_no} is not available"
                
                s.seat_status = seatAvailableStatus.RESERVED
                return f"Seat {seat_no} booked successfully in {self.flight_name}"
            
        return f"seat{seat_no} does not exist"


    def cancel_booking(self, seat_no):
        for s in self.available_seats:
            if s.seat_no == seat_no:
                s.seat_status = seatAvailableStatus.AVAILABLE
                return f"Seat {seat_no} cancelled"

        return "Seat not found"
        

    




    
