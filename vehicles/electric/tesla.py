from vehicles.vehicle import Vehicle
# Electric car
class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def charge_battery(self):
        print("Okay! Battery charged!")

    def drive(self):
        print(f"The {self.main_color} Tesla drives past. Zoooooooooooom!")

    def turn(self, direction):
        print(f"The Tesla silently makes a {direction} turn.")