class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_average(self):
        grades_sum = 0
        for grade in self.grades:
            grades_sum += grade
        return grades_sum/len(self.grades)

grades = [85.5, 90.0, 78.0]
student = Student("Emily", grades)
average = student.calculate_average()
print(average)