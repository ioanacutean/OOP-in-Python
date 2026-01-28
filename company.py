from employee import Employee

class Company():
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        for employee in self.employees:
            print(employee.first_name + " " + employee.last_name)

    def pay_employees(self):
        for employee in self.employees:
            print('Paycheck for:', employee.first_name, employee.last_name)
            print(f'Amount: ${employee.calculate_paycheck():,.2f}')
            print('---------------------------------------')

def main():
    my_company = Company()

    employee1 = Employee('John', 'Wayne', 25, 'Programmer', 10000)
    employee2 = Employee('Jane', 'Austen', 45, 'HR Specialist', 20000)
    employee3 = Employee('Will', 'Smith', 43, 'Data Analyst', 18000)
    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)
    employee1.increase_salary(10)
    my_company.display_employees()
    my_company.pay_employees()

    print(str(employee1))
    print(repr(employee1))
    print(eval(repr(employee1)))

    print(employee1.annual_salary)
    employee1.salary = 2000
    print(employee1.annual_salary)

    #Name mangling demonstration
    #print(employee1.__salary) #raises an AttributeError
    #print(employee1._Employee__salary)

if __name__ == '__main__':
    main()