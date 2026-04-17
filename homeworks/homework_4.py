"""1 задание"""

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        if len(phone_number) == 10 :
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} {self.phone_number}"



class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            raise ValueError("Invalid phone number")




print(ContactList.all_contacts)

ContactList.add_contact("Michael Jackson", "1111111111")
ContactList.add_contact("Viktor Tsoy", "2222222222")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number, sep = ", ")

ContactList.add_contact("Лена Ногти", "333333333")


"""2 задание"""

class Library:
    def __init__(self, city: str, books: list):
        self.city = city
        self.books = books

    def __str__(self):
        return f"<Library object, city: {self.city}, books: {len(self.books)}>"

    def __len__(self):
        return len(self.books)

    def __contains__(self, book):
        print(f"Ищем книгу: {book}")
        return book in self.books

    def __bool__(self):
        return True if len(self.books) > 5 else False

lib = Library("Бишкек", books=["Война и мир", "1984", "Мастер и Маргарита"])
print(lib)
print(len(lib))
print("1984" in lib)
print("Гарри Поттер" in lib)
if lib:
    print("Библиотека большая (более 5 книг)")
else:
    print("Библиотека маленькая")