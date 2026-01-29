from dataclasses import dataclass

@dataclass(slots=True)
class Project:

    name: str
    payment: int
    client: str

    def notify_client(self):
        print(f"Notifying the client about the progress of {self.name}...")

# class Project:
#     def __init__(self, name, payment, client):
#         self.name = name
#         self.payment = payment
#         self.client = client
#
# def notify_client(self):
#     print(f"Notifying the client about the progress of {self.name}...")

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


p = Project("Django App", 20000, "Globomantics")
e = Employee("Ioana", 29, 8000, p)
print(e.project)
