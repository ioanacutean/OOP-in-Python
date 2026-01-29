class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        if self.denominator == other.denominator:
            self.numerator += other.numerator
        else:
            (numerator_self, denominator_self, numerator_other) = self.make_common_denominator(other)
            self.numerator = numerator_self
            self.denominator = denominator_self
            self.numerator = numerator_self + numerator_other
            self.denominator = denominator_self
        self.reduce()

    def subtract(self, other):
        if self.denominator == other.denominator:
            self.numerator -= other.numerator
        else:
            (numerator_self, denominator_self, numerator_other) = self.make_common_denominator(other)
            self.numerator = numerator_self
            self.denominator = denominator_self
            self.numerator = numerator_self - numerator_other
            self.denominator = denominator_self
        self.reduce()

    @staticmethod
    def find_greatest_common_divisor(a, b):
        while b:
            a, b = b, a % b
        return a

    def reduce(self):
        gcd = self.find_greatest_common_divisor(self.numerator, self.denominator)
        self.numerator  = self.numerator // gcd
        self.denominator = self.denominator // gcd

    def make_common_denominator(self, other):
        numerator_self = self.numerator * other.denominator
        denominator_self = self.denominator * other.denominator
        numerator_other = other.numerator * self.denominator
        return numerator_self, denominator_self, numerator_other

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

f1 = Fraction(10, 3)
f2 = Fraction(6, 9)
f2.add(f1)
print(f1)
print(f2)
f3 = Fraction(3, 2)
f4 = Fraction(5, 4)
f3.subtract(f4)
print(f3)
print(f4)

