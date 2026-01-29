class Athlete:

    def __init__(self, name, sport):
        self.__name = name
        self.__sport = sport

    def __str__(self):
        return f"Name: {self.__name}, Sport: {self.__sport}"

    def display(self):
        print("Athlete info:")
        print(f"Name: {self.__name}, Sport: {self.__sport}")

class Scholar:

    def __init__(self, name, major):
        self.__name = name
        self.__major = major

    def __str__(self):
        return f"Name: {self.__name}, Major: {self.__major}"

    def display(self):
        print("Scholar info:")
        print(f"Name: {self.__name}, Major: {self.__major}")


class StudentAthlete(Athlete, Scholar):

    def __init__(self, name, sport, major, student_id):
        Athlete.__init__(self, name, sport)
        Scholar.__init__(self, name, major)
        self.student_id = student_id

    def __str__(self):
        return f"Name: {self._Athlete__name}, Sport: {self._Athlete__sport}, Major: {self._Scholar__major}, Student ID: {self.student_id}"

    def display(self):
        print("Athlete student's info:")
        print(f"Name: {self._Athlete__name}, Sport: {self._Athlete__sport} Major: {self._Scholar__major} Student ID: {self.student_id}")


athlete = Athlete("Charlie", "Basketball")
scholar = Scholar("Dana", "Physics")
student_athlete = StudentAthlete("Eve", "Soccer", "Biology", "SA12345")

print(athlete) # outputs: "Name: Charlie, Sport: Basketball"
print(scholar) # outputs: "Name: Dana, Major: Physics"
print(student_athlete) # outputs: "Name: Eve, Sport: Soccer, Major: Biology, Student ID: SA12345"

print()
athlete.display()
scholar.display()
student_athlete.display()