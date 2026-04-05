import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education


    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def age(self):
        month_of_birth = int(self.birth_date.split("-")[1])
        year_of_birth = int(self.birth_date.split("-")[2])
        day_of_birth = int(self.birth_date.split("-")[0])

        today = datetime.datetime.now()

        age = today.year - year_of_birth

        if (today.month, today.day) < (month_of_birth, day_of_birth):
            age -= 1

        return age

    def introduce(self):
        if self.higher_education:
            education = "высшее образование есть"
        else:
            education = "высшего образования нет"

        return f"Привет, меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, {education}."


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name, classmate_of):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
        self.classmate_of = classmate_of

    def introduce(self):
        if self.higher_education:
            education = "высшее образование есть"
        else:
            education = "высшего образования нет"
        return f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Я учился с {self.classmate_of} в группе {self.group_name}. У меня {education}"


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, friend_of):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.friend_of = friend_of

    def introduce(self):
        if self.higher_education:
            education = "высшее образование есть"
        else:
            education = "высшего образования нет"
        return f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Мое хобби {self.hobby}. У меня {education}. Я друг {self.friend_of}. "


class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, shared_memory, friend_of):
        super().__init__(name, birth_date, occupation, higher_education, hobby, friend_of)
        self.shared_memory = shared_memory

    def introduce(self):
        if self.higher_education:
            education = "высшее образование есть"
        else:
            education = "высшего образования нет"
        return (f"Привет, меня зовут {self.name}, я лучший друг {self.friend_of}, я родился {self.birth_date}, у меня {education}, работаю {self.occupation}, "
                f"мое хобби {self.hobby}. Наши совместные воспоминания: {self.shared_memory}.")


person = Person("Артур", "23-12-2009", "Программист", False)
classmate_1 = Classmate("Омурбек", "11-10-2009", "Дизайнер", False, "10A", person.name)
classmate_2 = Classmate("Эльдар", "21-05-2009", "Маркетолог", False, "10A", person.name)
friend_1 = Friend("Дастан", "01-09-2009", "Кинематограф", True, "Хоббихорсинг", person.name)
friend_2 = Friend("Илья", "05-05-2010", "Переводчик", False, "Рисования", person.name)
best_friend = BestFriend("Максим", "27-10-2009", "Сигмой", False, "Спорт", "Кушали кириешки вместе", person.name)




persons = [person, classmate_1, classmate_2, friend_1, friend_2, best_friend]
for prsn in persons:
    print(prsn.introduce())
    print(f"Возраст: {prsn.name} = {prsn.age}")