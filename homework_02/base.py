from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int
    started: int = False
    fuel: int
    fuel_consumption: int
    distance: int

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print("Автомобиль завёлся")
            else:
                raise LowFuelError("Нет топлива, необходимо заправиться")

    def move(self, distance):
        fuel_needed = self.fuel_consumption * distance
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
        else:
            raise NotEnoughFuel("Топлива не хватит на прохождение дистанции")
