from vehicles.vehicle import Vehicle
# Gas powered truck
class Ram(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
        print("All full!")

    def drive(self):
        print(f"The {self.main_color} Ram drives past. RRrrrrrummbbble!")