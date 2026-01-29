class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print("Driving a vehicle")

    def __str__(self):
        return f"Vehicle: {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def drive(self):
        print(f"Driving a {self.make} {self.model}")

    def __str__(self):
        return f"Car: {self.make} {self.model}"


class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def drive(self):
        print(f"Driving a {self.make} {self.model}")

    #when not defined inherited Vehicle __str__ will be used
    def __str__(self):
        return f"Bike: {self.make} {self.model}"


car = Car("Toyota", "Corolla")
bike = Bike("Yamaha", "YZF-R3")
car.drive() # outputs: "Driving a Toyota Corolla"
bike.drive() # outputs: "Riding a Yamaha YZF-R3"
print(car) # outputs: "Car: Toyota Corolla"
print(bike) # outputs: "Bike: Yamaha YZF-R3"
