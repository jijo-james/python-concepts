class Vehicle:
    def __init__(self, starting_position=0, time=0, speed=0):
        if time < 0:
            raise ValueError("Time must be a non-negative value")
        if speed < 0:
            raise ValueError("Speed must be a non-negative value")

        self.starting_position = starting_position
        self.time = time
        self.speed = speed

    def current_position(self):
        return self.starting_position + (self.speed * self.time)

    def distance(self, other_vehicle):
        return abs(self.current_position() - other_vehicle.current_position())


class Car(Vehicle):
    def __init__(self, starting_position=0, time=0, speed=0):
        super().__init__(starting_position, time, speed)


class Truck(Vehicle):
    def __init__(self, starting_position=100, time=0, speed=0):
        super().__init__(starting_position, time, speed)


class Bicycle(Vehicle):
    def __init__(self, starting_position=0, time=0, speed=0):
        super().__init__(starting_position, time, speed)


def convert_speed_to_mph(speed, unit):
    if unit == "mph":
        return speed
    elif unit == "kph":
        return speed * 0.621371  # Convert from kilometers per hour to miles per hour
    elif unit == "fpm":
        return speed / 88  # Convert from feet per minute to miles per hour


car = Car(starting_position=0, time=10, speed=50)
truck = Truck(starting_position=100, time=10, speed=40)
bicycle = Bicycle(starting_position=0, time=10, speed=50)

car_speed_mph = convert_speed_to_mph(car.speed, "mph")
truck_speed_mph = convert_speed_to_mph(truck.speed, "kph")
bicycle_speed_mph = convert_speed_to_mph(bicycle.speed, "fpm")

distance_car_truck = abs(car.current_position() - truck.current_position())
distance_car_bicycle = abs(car.current_position() - bicycle.current_position())

print(distance_car_truck)
print(distance_car_bicycle)
