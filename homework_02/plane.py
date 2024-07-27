"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    max_cargo: int
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.fuel = fuel
        self.weight = weight
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, amount):
        if self.cargo + amount <= self.max_cargo:
            self.cargo += amount
        else:
            raise CargoOverload("Автомобиль перегружен")

    def remove_all_cargo(self):
        res = self.cargo
        self.cargo = 0
        return res
