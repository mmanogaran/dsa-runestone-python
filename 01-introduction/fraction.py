def gcd(m, n):
    """Return the greatest common denominator (GCD) of m and n. Will return
    negative number if n is negative"""
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


class Fraction:
    def __init__(self, num, den):
        common = gcd(num, den)
        self.num = num // common
        self.den = den // common

    def __add__(self, other_fraction):
        new_num = (self.num * other_fraction.den) + (
            self.den * other_fraction.num
        )
        new_den = self.den * other_fraction.den

        return Fraction(new_num, new_den)

    def __sub__(self, other_fraction):
        return self.__add__(Fraction(-other_fraction.num, other_fraction.den))

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)

    def __eq__(self, other_fraction):
        return (self.num == other_fraction.num) and (
            self.den == other_fraction.den
        )

    def __str__(self):
        return "{}/{}".format(self.num, self.den)