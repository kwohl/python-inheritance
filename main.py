from vehicles import Cessna, Ram, Saab, Zero, Tesla, Vehicle

katie = Saab()
katie.main_color = "blue"
katie.maximum_occupancy = 5
katie.drive()
katie.turn("left")
katie.stop()

print()

kurt = Tesla()
kurt.main_color = "black"
kurt.drive()
kurt.turn("right")
kurt.stop()

print()

cooper = Cessna()
cooper.main_color = "aquamarine"
cooper.drive()
cooper.turn("left")
cooper.stop()

print()

roxanne = Zero()
roxanne.main_color = "purple"
roxanne.drive()
roxanne.turn("right")
roxanne.stop()

print()

andy = Ram()
andy.main_color = "red"
andy.drive()
andy.turn("left")
andy.stop()