from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """UnreliableCar class"""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """determines if car will drive"""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        return distance
