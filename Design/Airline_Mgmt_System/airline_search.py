from booking_flight_details import bookingFlight

class AirlineSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight: bookingFlight):
        self.flights.append(flight)

    def search_flight(self, source, destination):
        result = []
        for f in self.flights:
            if f.source == source and f.destination == destination:
                result.append(f)
        return result