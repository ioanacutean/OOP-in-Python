class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f'Car make: {self.make},  Model: {self.model}')

car = Car('Ford', 'Mustang')
car.display_info()