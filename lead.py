class Lead:
    def __init__(self, name, staff_size, estimated_revenue, effort_factor):
        self.name = name
        self.staff_size = staff_size
        self.estimated_revenue = estimated_revenue
        self.effort_factor = effort_factor

    @classmethod
    def get_digits_in(cls, element):
        nr_digits = 0
        while element > 0:
            nr_digits += 1
            element //= 10
        return nr_digits


    def calculate_lead_score(self):
        digits_in_revenue = self.get_digits_in(self.estimated_revenue)
        digits_in_staff_size = self.get_digits_in(self.staff_size)
        return 1 / (self.staff_size / self.estimated_revenue * (10 ** (digits_in_revenue - digits_in_staff_size)) * self.effort_factor)

    def __eq__(self, other):
        return self.calculate_lead_score() == other.calculate_lead_score()

    def __ne__(self, other):
        return self.calculate_lead_score() != other.calculate_lead_score()

    def __lt__(self, other):
        return self.calculate_lead_score() < other.calculate_lead_score()

    def __le__(self, other):
        return self.calculate_lead_score() <= other.calculate_lead_score()

    def __gt__(self, other):
        return self.calculate_lead_score() > other.calculate_lead_score()

    def __ge__(self, other):
        return self.calculate_lead_score() >= other.calculate_lead_score()

lead1 = Lead("Ion", 30, 10000, 5)
print(f'Lead score for {lead1.name} is {lead1.calculate_lead_score()}')
lead1.staff_size = 70
lead1.estimated_revenue = 50000
print(f'Updated lead score for {lead1.name} is {lead1.calculate_lead_score()}')

lead2 = Lead("Daniel", 20, 10000, 3)
print(f'Lead score for {lead2.name} is {lead2.calculate_lead_score()}')

print(lead1 == lead2)
print(lead1 == lead1)

if lead1 > lead2:
    print(f'{lead1.name} has higher lead score than {lead2.name}.')
elif lead1 < lead2:
    print(f'{lead1.name} has lower lead score than {lead2.name}.')
else:
    print(f'{lead1.name} has the same lead score as {lead2.name}.')
