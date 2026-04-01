class Person():
    def __init__(self, name, birth_date, occupation, higher_education: bool):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        return (f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, {'высшее' if self.higher_education == True else 'высшего'} "
                f"образования {'нет' if self.higher_education == False else 'есть'}. ")

person_1 = Person("Артур", "23-12-2009", "Программист", False)
person_2 = Person("Максим", "27-10-2009", "Дизайнер", False)
person_3 = Person("Омурбек", "11-10-2009", "Кинематограф", True)
print(person_1.introduce(), vars(person_1), sep = "Атрибуты: ")
print(person_2.introduce(), vars(person_2), sep = "Атрибуты: ")
print(person_3.introduce(), vars(person_3), sep = "Атрибуты: ")