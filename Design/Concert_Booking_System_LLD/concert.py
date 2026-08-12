from typing import List
from seat import Seat
class Concert:
    def __init__(self, concert_id, artist, venue, date, time):
        # unique id of the concert
        self.concert_id = concert_id
        # artist name
        self.artist = artist
        # venue name
        self.venue = venue
        # date of concert
        self.date = date
        # time of concert
        self.time = time
        # this will store all the seat objects for this concert
        self.seats: List[Seat] = [] # empty list at start, can add Seat objects later

    # method to show available seats
    def show_available_seats(self):
        # create empty list to store available seat numbers
        available = []
        # loop through each seat in seats
        for seat in self.seats:
            # if seat is not booked, add to available list
            if seat.is_booked == False:
                available.append(seat.seat_number)
        return available
    
    def add_seat(self, seat: Seat):
        # add the Seat object to the seats list
        self.seats.append(seat)