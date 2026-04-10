class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age



    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        print(f"Прошлый возвраст {self.__age}, новый возраст {new_age}")
        self.__age = new_age


    def make_sound(self):
        return "Животное издает звук"


class Dog(Animal):
    def make_sound(self):
        return "Собака гавкает"

class Cat(Animal):
    def make_sound(self):
        return "Кошка мяукает"

dog = Dog("Шарик", 10)
cat = Cat("Барсик", 6)

cat.set_age(10)
print(cat.make_sound())
print(cat.get_age())

print(dog.make_sound())
print(dog.get_age())
print(dog.get_name())
dog.set_name("Гавнобобик")
dog.set_age(20)
print(dog.get_age())
print(dog.get_name())