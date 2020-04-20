from vehicles.vehicle import Vehicle
# Electric motorcycle
class Zero(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def charge_battery(self):
        print("Okay! Battery is charged!")

    def drive(self):
        print(f"The {self.main_color} Zero zips past! Zoom zoom!")

    def stop(self):
        print("The Zero comes to a sharp stop!")

    def turn(self, direction):
        print(f"The Zero zips around another car to make a {direction} turn.")
