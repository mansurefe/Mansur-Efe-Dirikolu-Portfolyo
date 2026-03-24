from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand , model, year,):
        self._brand = brand
        self._model = model
        self._year = year

    @property
    def brand(self):
        return self._brand

    @abstractmethod
    def show_info(self):
        pass

class Car(Vehicle):
        def __init__(self, brand, model, year, fuel_type):
            super().__init__(brand, model, year)
            self.fuel_type = fuel_type # yani benzin mi dizel mi elektrikli mi
            self.kilometers = 0
            self.fuel_consumed = 0

        def drive(self, distance_km):
            self.kilometers += distance_km
            print(f"{self.brand} drove {distance_km} km. Total: {self.kilometers} km.")

        def refuel(self, liters):
            self.fuel_consumed += liters
            print(f"{self.brand} refueled {liters} liters. Total fuel: {self.fuel_consumed} L.")

        def fuel_efficiency(self):
            if self.kilometers == 0:
                return "Car has not been driven yet."
            efficiency = self.kilometers / self.fuel_consumed
            return f"Fuel efficiency: {efficiency:.2f} km/l"

        def show_info(self):
            print(f"Brand: {self.brand}")
            print(f"Model: {self._model}")
            print(f"Year: {self._year}")
            print(f"Fuel Type: {self.fuel_type}")
            print(f"Kilometers: {self.kilometers}")
            print(f"Fuel Consumed: {self.fuel_consumed} L")

renault = Car("Renault", "Clio", 2018, "LPG")
renault.drive(120)
renault.refuel(10)
renault.show_info()
print(renault.fuel_efficiency())