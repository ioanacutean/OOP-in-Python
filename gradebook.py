from student_class import Student

class Gradebook:
    students = []
    def __init__(self, capacity):
        self.capacity = capacity

    def add_student(self, student):
        if len(self.students) == self.capacity:
            print("The gradebook is full.")
        else:
            self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.get_info()

    def calculate_class_average(self):
        total = 0
        for student in self.students:
            total += student.average_grade
        return total / len(self.students)

    def find_top_student(self):
        top_average_grade = 0
        top_student = None
        if len(self.students) == 0:
            print("No student found")
        else:
            for student in self.students:
                if student.average_grade > top_average_grade:
                    top_average_grade = student.average_grade
                    top_student = student.name

        return top_student

gradebook = Gradebook(2)
# Create Student objects
s1 = Student("Alice", [85, 90, 78])
s2 = Student("Bob", [92, 88, 95])
s3 = Student("Charlie", [70, 75, 80])
# Add students individually
gradebook.add_student(s1)
gradebook.add_student(s2)
# Attempt to add another student
gradebook.add_student(s3) # Should print a message indicating the gradebook is full
# Display all students
gradebook.display_all_students()
# Calculate and display class average
print(f"Class Average: {gradebook.calculate_class_average():.2f}")
# Find and display the top student
print(f"Top Student: {gradebook.find_top_student()}")