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
class Classmate(Person):
    def __init__(self,name,birth_date,occupation,higher_education,body_length):
        super().__init__(name,birth_date,occupation,higher_education)
        self.body_length = body_length

    def introduce(self):
        print(f'имя = {self.name}\n'
              f'дата рождения = {self.birth_date}\n'
              f'место работы = {self.occupation}\n'
              f'наличиее вышего образование = {self.higher_education}\n'
              f'рост тело состовляет = {self.body_length}\n')
class Friend(Person):
    def __init__(self,name,birth_date,occupation,higher_education, weight):
        super().__init__(name,birth_date,occupation,higher_education)
        self.weight = weight

    def introduce(self):
        print(f'имя = {self.name}\n'
              f'дата рождения = {self.birth_date}\n'
              f'место работы = {self.occupation}\n'
              f'наличиее вышего образование = {self.higher_education}\n'
              f'масса тело состовляет = {self.weight}')
cl_azamat = Classmate('Azamat', '01.04.2007','нету',False,'1.76 cm')
fr_kirsan = Friend('Kirsan','03.12.2007','нету',False,'63 kg')
print(cl_azamat.introduce())
print(fr_kirsan.introduce())