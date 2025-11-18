class Distance:
    def __init__(self,value,unit):
        self.value = value
        self.unit = unit

    def convert(self):
        if self.unit == 'km':
            return self.value * 1000
        elif self.unit == 'mm':
            return self.value / 1000
        elif self.unit == 'cm':
            return self.value / 100
        else:
            return self.value

    def __add__(self, other):
        add = self.convert() + other.convert()
        return f'{add} m'

    def __sub__(self, other):
        sub = self.convert() - other.convert()
        return f'{sub} m'

    def __eq__(self,other):
        return self.convert() == other.convert()

value1=Distance(1,'km')
value2=Distance(1000,'m')
print(f'__add__:{value1+value2}')
print(f'__sub__:{value1-value2}')
print(f'__eq__:{value1==value2}')