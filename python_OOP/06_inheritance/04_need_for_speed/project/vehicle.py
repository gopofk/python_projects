class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.horse_power = horse_power
        self.fuel = fuel
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        curr_consumption = self.fuel_consumption * kilometers

        if self.fuel >= curr_consumption:
            self.fuel -= curr_consumption
            return self.fuel
