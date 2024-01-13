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
    def __init__(self, starting_position=10, time=0, speed=0):
        super().__init__(starting_position, time, speed)


class Truck(Vehicle):
    def __init__(self, starting_position=100, time=0, speed=0):
        super().__init__(starting_position, time, speed)


class Bicycle(Vehicle):
    def __init__(self, starting_position=0, time=0, speed=0):
        super().__init__(starting_position, time, speed)


car = Car()
print(car.starting_position)

car = Car(starting_position=0, time=10, speed=50)
print(car.starting_position)

truck = Truck()
print(truck.starting_position)

truck.starting_position = 50
truck.time = 10
truck.speed = 40
print(car.distance(truck))
