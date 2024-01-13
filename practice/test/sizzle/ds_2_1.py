class Car:
    def __init__(self, color, weight_kg, parts, accident_history, license_info):
        self.color = color
        self.weight_kg = weight_kg
        self.parts = parts
        self.accident_history = sorted(set(accident_history))
        self.license_info = license_info


class LicenseInfo:
    def __init__(self, state, plate_number, expiration_date):
        self.state = state
        self.plate_number = plate_number
        self.expiration_date = expiration_date


class Component:
    def __init__(self, name):
        self.name = name
