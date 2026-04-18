
import random

"""Player"""
class Player:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.is_defending = False
    def __str__(self):
        return f"Игрок {self.name} | {self.health} HP | Урон: {self.damage}"
    def attack_other(self, other) -> str:
        chance = random.randint(1, 5)
        if chance == 1 and other.is_defending == False:
            critical_damage = random.randint(8, 20)
            other.health = other.health - (self.damage + critical_damage)
            return f"{self.name}, вы атаковали {other.name} на {self.damage} HP, но плюс еще крит {critical_damage}, у {other.name} осталось {other.health} HP"
        elif chance > 1 and chance <= 5 and other.is_defending == False:
            other.health -= self.damage
            return f"{self.name}, вы атаковали {other.name} на {self.damage} HP, у {other.name} осталось {other.health} HP"
        else:
            other.is_defending = False
            return f"{other.name} отразил вашу атаку и его защита сломана"
    def is_alive(self) -> bool:
        return True if self.health > 0 else False
    def heal(self) -> str:
        if self.health >= 81:
            return "Вы пока что не можете хилиться"
        elif 0 < self.health < 81:
            healing = random.randint(10, 20)
            self.health += healing
            return f"Вы восстановились на {healing} здоровья, теперь у {self.name} {self.health}HP"
    def defend(self) -> str:
        chance = random.randint(1, 2)
        if chance == 1:
            self.is_defending = True
            return "Вы успешно отразите следующую атаку"
        elif chance == 2:
            return "Вам не удалось отразить атаку"


def checking_move(current_move):
    if current_move == 0:
        return random.randint(1,2)
    elif current_move == 1:
        return 2
    elif current_move == 2:
        return 1

def check_translation(name):
    eng = "q w e r t y u i o p [ ] a s d f g h j k l ; ' z x c v b n m , . / ".split()
    rus = "й ц у к е н г ш щ з х ъ ф ы в а п р о л д ж э я ч с м и т ь б ю . ".split()
    eng_upper = 'Q W E R T Y U I O P { } A S D F G H J K L : " Z X C V B N M < >'.split()
    rus_upper = "Й Ц У К Е Н Г Ш Щ З Х Ъ Ф Ы В А П Р О Л Д Ж Э Я Ч С М И Т Ь Б Ю".split()
    answer = ""
    count = 0
    for i in name:
        if i in eng or i in eng_upper:
            if i in eng:
                answer += rus[eng.index(i)]
                count += 1
            elif i in eng_upper:
                answer += rus_upper[eng_upper.index(i)]
                count += 1
        elif i in rus:
            answer += rus[rus.index(i)]
        else:
            answer += i
    if count >= 1:
        ask = input(f"Изменить ли ваше имя на {answer}? Или вы хотите оставить {name}?, введите Y если поменять, N если оставить: ")
        if ask.lower() == "y":
            return answer
        elif ask.lower() == "n":
            return name
    elif count == 0:
        return name



current_move = 0
list_of_moves = ("attack", "heal", "defend")
player1 = Player(check_translation(input("Введите имя для первого игрока: ")).capitalize(), 100, random.randint(10, 50))
player2 = Player(check_translation(input("Введите имя для второго игрока: ")).capitalize(), 100, random.randint(10, 50))
print(f"- Урон игрока {player1.name} - {player1.damage} \n- Урон игрока {player2.name} - {player2.damage}")

current_move = checking_move(current_move)
"""Игра"""
while player1.is_alive() and player2.is_alive():
    try:
        if current_move == 1:
            print(f"Очередь ходить игрока {player1.name}")
            ask = input(f"Игрок {player1.name} пожалуйста введите действие которое вы хотите сделать, вот список действий: {list_of_moves}: ").lower()
            if ask in list_of_moves and ask == "attack":
                print(player1.attack_other(player2))
            elif ask in list_of_moves and ask == "heal":
                print(player1.heal())
            elif ask in list_of_moves and ask == "defend":
                print(player1.defend())
            elif ask not in list_of_moves:
                print("Вы ввели неправильную команду, попробуйте еще раз")
                continue
            current_move = checking_move(current_move)
        elif current_move == 2:
            print(f"Очередь ходить {player2.name}")
            ask = input(f"Игрок {player2.name} пожалуйста введите действие которое вы хотите сделать, вот список действий: {list_of_moves}: ").lower()
            if ask in list_of_moves and ask == "attack":
                print(player2.attack_other(player1))
            elif ask in list_of_moves and ask == "heal":
                print(player2.heal())
            elif ask in list_of_moves and ask == "defend":
                print(player2.defend())
            elif ask not in list_of_moves:
                print("Вы ввели неправильную команду, попробуйте еще раз")
                continue
            current_move = checking_move(current_move)
    except ValueError:
        print(f"Вы ввели неправильное значение команды, она должна состоять только из данных команд {list_of_moves}")
else:
    if player1.is_alive():
        print(f"Игрок {player2.name} мертв. ПОЗДРАВЛЯЕМ С ПОБЕДОЙ {player1.name}")
    elif player2.is_alive():
        print(f"Игрок {player1.name} мертв. ПОЗДРАВЛЯЕМ С ПОБЕДОЙ {player2.name}")



# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         return f"Ваш баланс: {self.__balance}"
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance -= amount
#             return f"Вы успешно пополни баланс на {amount}"
#         else:
#             return f"Вы ввели неправильную сумму депозита"
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             return f"Вы успешно пополнили баланс на {amount}"
#         else:
#             return f"Вы ввели неправильную сумму снятия"
#
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#     @property
#     def price(self):
#         return f"Цена продукта - {self.__price}"
#
#     @price.setter
#     def set_price(self, new_price):
#         if new_price > 0:
#             self.__price = new_price
#             return f"Вы установили цену продукта {self.name} на {self.__price}"
#         else:
#             return f"Вы ввели неправильную цену для товара"

#
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Order:
#     def __init__(self):
#         self.__price = 0
#         self.products = []
#
#     @property
#     def price(self):
#         return self.__price
#
#     def add_object(self, product):
#         if product.price > 0:
#             self.products.append(product)
#             self.__price += product.price
#             return f"Вы успешно добавили товар: {product.name}, стоимостью {product.price}, актуальная сумма заказа {self.__price}"
#         else:
#             return "Добавлен объект с неправильной ценой"
#
#
# class CardPayment:
#     def pay(self, order):
#         return f"Вы оплатили заказ картой на сумму: {order.price}"
#
#
# class CashPayment:
#     def pay(self, order):
#         return f"Вы оплатили заказ наличкой на сумму: {order.price}"
#
#
# def poli(method, order):
#     return method.pay(order)
#
#
# product1 = Product("sigma", 100)
# product2 = Product("mouse", 250)
#
# order = Order()
#
# print(order.add_object(product1))
# print(order.add_object(product2))
#
# card = CardPayment()
# cash = CashPayment()
#
# print(poli(card, order))
# print(poli(cash, order))

class Package:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
            print(f"Вес {value} kg успешно установлен")
        else:
            print(f"Неправильно введен вес")



class CarDelivery:
    def deliver(self, package):
        return f"Посылка {package.name} доставлена за цену {package.weight * 100}"

class AirDelivery:
    def deliver(self, package):
        return f"Посылка {package.name} доставлена за цену {package.weight * 250}"

class ShipDelivery:
    def deliver(self, package):
        return f"Посылка {package.name} доставлена за цену {package.weight * 150}"

def delivery(type_of_delivery, package):
    return type_of_delivery.deliver(package)

package = Package("Ноутбук", 2)
car_delivery = CarDelivery()
ship_delivery = ShipDelivery()
air_delivery = AirDelivery()

print(delivery(car_delivery, package))
