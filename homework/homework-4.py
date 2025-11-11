class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    @staticmethod
    def validate_phone_number(phone_number):
        return len(phone_number) == 10
class ContactList:
    all_contacts = []
    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)
        else:
            raise ValueError('Неверный формат номера телефона!!! \nОн должен состоять из 10 цифр!')
quantity = int(input('Введите количество контактов которых хотите добавить: '))
for i in range(quantity):
    name = input('Имя: ')
    phone = input('Номер телефона (10 цифр): ')
    try:
        ContactList.add_contact(name, phone)
    except:
        raise ValueError('неверный контактный номер')

print('\nСписок контактов')

for contact in ContactList.all_contacts:
    print(f'имя:{contact.name}, \nномер телефона:{contact.phone_number}',sep='\n')