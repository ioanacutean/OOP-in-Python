class Student:
    average_grade = None

    def __init__(self, name, grades):
        self.name = name
        self._grades = grades
        self.set_average_grade()

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, value):
        if len(self.grades) == 0:
            print("The student has no grades.")
        else:
            self._grades = value

    def calculate_average(self):
        average = None
        if len(self.grades) == 0:
            print("The student has no grades.")
        else:
            average = sum(self.grades) / len(self.grades)
        return average

    def set_average_grade(self):
        self.average_grade = self.calculate_average()

    def get_info(self):
        print(f"The student {self.name} has an average grade of {self.average_grade:.2f}")

    def __str__(self):
        print(f"The student {self.name} has an average grade of {self.average_grade:.2f}")
