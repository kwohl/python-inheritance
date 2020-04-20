from vehicles.vehicle import Vehicle
# Propellor light aircraft
class Cessna(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
        print("All full!")

    def drive(self):
        print(f"The {self.main_color} Cessna flies overhead. Whiiiiiiirrrrr!")

    def turn(self, direction):
        print(f"The Cessna leans to the {direction}.")

    def stop(self):
        print(f"The {self.main_color} Cessna rolls to a stop after going a mile down the runway.")