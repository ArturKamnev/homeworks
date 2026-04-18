class Animal:
    def move(self):
        print("Moving animal")

class Swiming(Animal):
    def move(self):
        super().move()
        print("Swimming")

class Flying(Animal):
    def move(self):
        super().move
        print("Flying")

class Duck(Flying, Swiming):
    def move(self):
        super().move
        print("Утка плавает и летает")

duck = Duck()
duck.move()