from datetime import date
from way_enum import Way

class user_details:

    def __init__(self, u_name, u_id, u_add, u_flight_name, u_mail_id, u_destination, booking_date, u_way: Way, u_seat_booking_count):
        self.u_name = u_name
        self.u_id = u_id
        self.u_add = u_add
        self.u_flight_name = u_flight_name
        self.u_mail_id = u_mail_id
        self.u_destination = u_destination
        self.booking_date = booking_date
        self.u_way = u_way 
        self.u_seat_booking_count = u_seat_booking_count

    def get_name(self):
        return self.u_name

    def get_u_id(self):
        return self.u_id

    def get_u_flight_name(self):
        return self.u_flight_name

    def get_u_seat_booking_count(self):
        return self.u_seat_booking_count

    def get_user_details(self):
        return f"{self.u_name} is booking for {self.u_destination} on date {self.booking_date} for way {self.u_way.value} from the flight {self.u_flight_name}"