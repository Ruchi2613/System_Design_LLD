from seat_enum import seatTypes, seatAvailableStatus

class seat:
    def __init__(self, seat_id, seat_no, seat_type: seatTypes):
        self.seat_id = seat_id
        self.seat_no = seat_no
        self.seat_type = seat_type
        self.seat_status = seatAvailableStatus.AVAILABLE

    def get_seat_id(self):
        return self.seat_id

    def get_seat_no(self):
        return self.seat_no

    def get_seat_type(self):
        return self.seat_type

    def get_seat_status(self):
        return self.seat_status

    def seat_reserve(self):
        self.seat_status = seatAvailableStatus.RESERVED

    def seat_free(self):
        self.seat_status = seatAvailableStatus.AVAILABLE