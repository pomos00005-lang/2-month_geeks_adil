class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
    def make_sound(self):
        print('животное издает звук.')

    @name.setter
    def name(self, name2):
        self.__name = name2

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f'{self.name} это пес,ему {self.age} год(-а) и он издает звук "гав-гав"')

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f'{self.name} это кошка,ей {self.age} год(-а) и она издает звук "мяу-мяу"')

alpha = Dog('alpha',3)
kisa = Cat('kisa',1)


kisa.set_name = kisa.name.upper()

alpha.name = alpha.name.upper()
kisa.name = kisa.name.upper()


alpha.make_sound()
kisa.make_sound()