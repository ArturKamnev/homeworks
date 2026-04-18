class Car:
    def __init__(self, color, horse_power):
        self.color = color
        self.horse_power = horse_power

    def drive_to(self, destination):
        print(f"Car color {self.color} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color

class Bus(Car):
    def __init__(self, color, horse_power, passengers):
        super().__init__(color, horse_power)
        self.passengers = passengers

    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Bus color {self.color} driving to {destination}")

class Truck(Car):
    def change_color(self, new_color):
        print(f"Truck color {self.color} changed to {new_color}")
        self.color = new_color

bus_38 = Bus("green", 200, 38)
# print("Bus object is a bus?: ", isinstance(bus_38, Bus))
# print("Bus object is a car?: ", isinstance(bus_38, Car))
truck = Truck("red", 200)
car = Car("green", 200)
vehicles = [truck, car, bus_38]
for v in vehicles:
    v.drive_to("Караганда")