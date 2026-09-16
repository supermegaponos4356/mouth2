class Contact:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone = phone_number

    @staticmethod
    def validate_phone_number(phone_number: str) -> bool:
        return phone_number.isdigit() and len(phone_number) == 10


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name: str, phone_number: str):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            raise ValueError(f"Некорректный номер телефона: {phone_number}. Должно быть ровно 10 цифр.")


print(ContactList.all_contacts)

ContactList.add_contact("Иван Иванов", "0700100200")
ContactList.add_contact("Анна Петрова", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone)

ContactList.add_contact("Алексей Смирнов", "5551234")
