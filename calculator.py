class Calculator:
    __operation_count = 0

    def __init__(self):
        self.__operation_count = 0
        print("Calculator ready for use")

    @classmethod
    def add(cls, a, b):
        cls.__operation_count += 1
        return a + b

    @classmethod
    def subtract(cls, a, b):
        cls.__operation_count += 1
        return a - b

    @classmethod
    def multiply(cls, a, b):
        cls.__operation_count += 1
        return a * b

    @classmethod
    def divide(cls, a, b):
        if b == 0:
            result = float('NaN')
        else:
            cls.__operation_count += 1
            result = a / b

        return result

    @classmethod
    def get_operation_count(cls):
        return cls.__operation_count

    @classmethod
    def __str__(self):
        return f"Calculator with {self.__operation_count} operations performed."

# Perform operations using static methods from the Calculator class
sum_result = Calculator.add(5.0, 3.0) # returns 8.0
diff_result = Calculator.subtract(10.0, 4.0) # returns 6.0
product_result = Calculator.multiply(2.0, 3.5) # returns 7.0
quotient_result = Calculator.divide(20.0, 4.0) # returns 5.0

#Attempt division by zero
error_quotient = Calculator.divide(10.0, 0.0)
if error_quotient != error_quotient: # Check for NaN
 print("Division by zero encountered.")

# Display the number of operations performed
c = Calculator()
print("Total operations performed:", Calculator.get_operation_count())
print(c) # outputs: "Calculator with 5 operations performed"