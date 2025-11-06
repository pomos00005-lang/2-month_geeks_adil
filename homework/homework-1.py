class Person:
    def __init__(self, name, birth_date,occupation,higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f'имя = {self.name}\n'
              f'дата рождения = {self.birth_date}\n'
              f'место работы = {self.occupation}\n'
              f'наличиее вышего образование = {self.higher_education}\n')

person_Adil = Person('Адиль','03.01.2008','без работный',False)
person_Azim = Person("Азим",'04.04.2006',"Прораб",True)
person_Azim.introduce()
person_Adil.introduce()
