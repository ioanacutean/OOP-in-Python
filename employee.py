class Employee:
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
        if new_salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._salary = new_salary
        self._annual_salary = None

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary
