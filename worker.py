class Worker:
    __worker_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Worker.__worker_count += 1

    @classmethod
    def get_worker_count(cls):
        return cls.__worker_count

    def display(self):
        print(f"Worker: {self.name}, Salary: {self.salary}")

    def __str__(self):
        return f"Worker {self.name} has the salary {self.salary}."

worker1 = Worker("Alice", 50000)
worker2 = Worker("Bob", 60000)
worker1.display() # outputs: "Name: Alice, Salary: 50000"
worker2.display() # outputs: "Name: Bob, Salary: 60000"
print(Worker.get_worker_count()) # outputs: 2
print(worker1) # outputs: "Employee: Alice with salary 50000"
print(worker2) # outputs: "Employee: Bob with salary 60000