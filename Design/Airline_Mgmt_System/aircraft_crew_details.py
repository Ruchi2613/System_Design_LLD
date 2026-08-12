class Aircraft:
    def __init__(self, aircraft_id, model):
        self.aircraft_id = aircraft_id
        self.model = model


class Crew:
    def __init__(self, crew_id, name, role):
        self.crew_id = crew_id
        self.name = name
        self.role = role