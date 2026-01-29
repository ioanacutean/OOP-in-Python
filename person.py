class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    def __str__(self):
       return f"The person {self.__name} is {self.__age} years old.."


class Student(Person):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id

    def display(self):
        print(f"Name: {self._Person__name}, Age: {self._Person__age}, Student ID: {self.__student_id}")

    def __str__(self):
        return f"The student {self._Person__name} is {self._Person__age} years old and has the ID: {self.__student_id}."

person = Person("Alice", 30)
student = Student("Bob", 20, "S12345")

print(person)
print(student)
student.display()
person.display()