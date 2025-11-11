class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self,location):
        print(f'{self.model} is driving in {location}')

    def test(self):
        self.drive('karakol')

color = "red"

car_honda = Car(color='red', model='Honda')
car_subaru = Car(color='silver', model='Subaru')

car_subaru.drive(location='Bishkek')

# print(car_honda)
# print(car_subaru)

print(car_subaru.color)
print(car_honda.color)
print(car_subaru.color == car_honda.color)