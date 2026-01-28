class Airplane:
    destinations = ['Havana', 'Athens', 'Teheran', 'New York']
    
    def __init__(self, model, manufacturer, capacity, current_passengers = 0, destination = 'Unknown'):
        self.model = model
        self.manufacturer = manufacturer
        self.capacity = capacity
        self.current_passengers = current_passengers
        self._destination = destination
        if destination != 'Unknown':
            self.destination = destination

    @property
    def current_passengers(self):
        return self._current_passengers

    @current_passengers.setter
    def current_passengers(self, new_passengers):
        if new_passengers < 0:
            print('Passengers cannot be negative')
        elif new_passengers > self.capacity:
            print(f'Can\'t board all passengers. Only {self.available_seats()} seats left.')
            self._current_passengers += self.available_seats()
        else:
            self._current_passengers = new_passengers
            
    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destination(self, new_destination):
        if new_destination not in self.__class__.destinations:
            print('Destination not in the list. It must be one of', self.__class__.destinations)
        else:
            self._destination = new_destination

    def board_passengers(self, number):
        self.current_passengers += number

    def disembark_passengers(self, number):
        self.current_passengers -= number

    def fly_to(self, new_destination):
        self.destination = new_destination

    def display_info(self):
        print('Airplane information:', end=', ')
        print(f'Model: {self.model}', end=', ')
        print(f'Manufacturer: {self.manufacturer}', end=', ')
        print(f'Capacity: {self.capacity}', end=', ')
        print(f'Current Passengers: {self.current_passengers}', end=', ')
        print(f'Destination: {self.destination}', end=' ')
        print()

    def available_seats(self):
        return self.capacity - self.current_passengers

    def is_full(self):
        return self.capacity == self.current_passengers


airplane = Airplane("Boeing 737", "Boeing", 180)
airplane.display_info()

airplane.board_passengers(150)
airplane.display_info()

seatsLeft = airplane.available_seats()
airplane.board_passengers(40)
airplane.display_info()

full = airplane.is_full()
airplane.fly_to("New York")
airplane.display_info()

airplane.disembark_passengers(50)
airplane.display_info()

airplane.disembark_passengers(30)
airplane.display_info()

seats_left = airplane.available_seats()
print('Seats left:', seats_left)

airplane1 = Airplane("Tarom 123", "Tarom", 120)
airplane.fly_to("Bucharest")
airplane.display_info()
airplane.fly_to("Havana")
airplane.display_info()
