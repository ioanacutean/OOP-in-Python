from datetime import date

class Employee:
    minimum_wage = 1000         # class attribute

    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError('Company is bankrupt.')
        cls.minimum_wage = new_wage

    @classmethod
    #calculate the age from date of birth and instantiates the employee with default value from salary
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

    def __init__(self, fname, lname, age, position, salary):
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None

    def increase_salary(self, percent):
        self._salary += self._salary * percent/100

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old. Employee is a {self.position}with the salary of ${self.salary}."

    def calculate_paycheck(self):
        return self.salary / 52  # 52 weeks

    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.first_name)}, {repr(self.last_name)}, "
            f"{repr(self.age)}, {repr(self.position)}, {repr(self.salary)})"
        )

    @property
    def salary(self):
        return self._salary


    @salary.setter
    def salary(self, new_salary):
        if new_salary < self.__class__.minimum_wage:
            raise ValueError('Minimum wage is $1000')
        self._salary = new_salary
        self._annual_salary = None

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary

print(Employee.minimum_wage)
Employee.change_minimum_wage(500)
print(Employee.minimum_wage)
