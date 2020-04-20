from vehicles.vehicle import Vehicle
#gas powered car
class Saab(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
        print("All full!")

    