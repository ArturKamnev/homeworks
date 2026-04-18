class Car:
    def __init__(self, color, horse_power):
        self.color = color
        self.horse_power = horse_power
        self._fined = True

    def _calculate_fule(self):
        return f"{self._fined}"

    def drive_to(self, destination):
        print(f"Car color {self.color} driving to {destination}")

    def change_color(self, new_color):
        self.color = new_color