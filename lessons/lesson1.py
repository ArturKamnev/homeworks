# class Sigma:
#     def __init__(self, answer, name):
#         self.answer = answer
#         self.name = name
#     def send_answer(self):
#         if self.answer == "hello":
#             return f"Hello {self.name}!"
#         elif self.answer == "poka":
#             return f"Poka {self.name}!"
#
# hi = input()
# if hi.startswith("hello"):
#     answer = "hello"
#     name = hi.split()[1]
# elif hi.startswith("poka"):
#     answer = "poka"
#     name = hi.split(" ")[1]
# sigma = Sigma(answer, name)
# print(sigma.send_answer())


class Car:  
    def __init__(self, color, horse_power):
        self.color = color
        self.horse_power = horse_power
    def drive_to(self, destination):
        return f"Car color {self.color}, destination {destination}, color changed to {self.change_color('другой')}"
    def change_color(self, new_color):
        self.color = new_color
        return self.color


car_1 = Car("silver", 1000)
car_2 = Car("black", 2500)
print(car_1.drive_to("араганда"))