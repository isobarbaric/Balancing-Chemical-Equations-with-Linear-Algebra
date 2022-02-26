
from math import gcd

# this Fraction class stores all of the relevant functionality needed to model fractions
class Fraction:

    # initializing a Fraction object with default denominator being 1
    def __init__(self, num, den = 1):
        # this assertion prevents an undefined fraction from being initialized 
        assert den != 0

        # simplification to simplest form
        self.num = int(num/gcd(num, den))
        self.den = int(den/gcd(den, num))

    # this overloads the addition operator for fractions so that fraction objects can be added
    def __add__(self, other):
        # determining the numerator and denominator for the new fraction        
        nBottom = (self.den*other.den)/gcd(self.den, other.den)
        nTop = self.num*(nBottom/self.den) + other.num*(nBottom/other.den)

        # if the numerator is 0, the entire fraction is effectively 0, regardless of what value the denominator has
        if (nTop == 0):
            return Fraction(0)

        # simplification to simplest form
        gcd_2 = gcd(int(nTop), int(nBottom))
        nTop /= gcd_2
        nBottom /= gcd_2

        # only one of the numerator and the denominator must contain a negative sign
        if (nBottom < 0):
            nTop *= -1
            nBottom *= -1
        return Fraction(int(nTop), int(nBottom))

    # this overloads the subtraction operator for fractions so that fraction objects can be subtracted
    def __sub__(self, other):
        return self.__add__(-1*other)

    # this overloads the addition operator for fractions so that fraction objects can be added
    def __mul__(self, other):
        # if the entity being multiplied is a numerical value, then it is to be dealt with separately from the case where the entity is another fraction
        if isinstance(other, (int, float)):
            nTop = self.num*other
            nBottom = self.den
        else:                
            assert type(other) is Fraction
            nTop = self.num*other.num
            nBottom = self.den*other.den

        # if the numerator is 0, the entire fraction is effectively 0, regardless of what value the denominator has
        if (nTop == 0):
            return Fraction(0)

        # simplification to simplest form
        gcd_2 = gcd(int(nTop), int(nBottom))
        nTop /= gcd_2
        nBottom /= gcd_2

        # only one of the numerator and the denominator must contain a negative sign
        if (nBottom < 0):
            nTop *= -1
            nBottom *= -1
        return Fraction(int(nTop), int(nBottom))

    # this builds on top of the multiplication operator for fractions so that multiplication can occur both with integers in front and integers after a fraction object
    def __rmul__(self, other): 
        return self.__mul__(other)

    # this overloads the division operator for fractions so that fraction objects can be divided
    def __truediv__(self, other):
        # determines the numerator and denominator for the new fraction
        nTop = self.num*other.den
        nBottom = self.den*other.num
 
        # if the numerator is 0, the entire fraction is effectively 0, regardless of what value the denominator has
        if (nTop == 0):
            return Fraction(0)

        # simplification to simplest form
        gcd_2 = gcd(int(nTop), int(nBottom))
        nTop /= gcd_2
        nBottom /= gcd_2

        # only one of the numerator and the denominator must contain a negative sign
        if (nBottom < 0):
            nTop *= -1
            nBottom *= -1
        return Fraction(int(nTop), int(nBottom))

    # defining how a fraction is to be printed 
    def __repr__(self):
        # if the denominator is equal to 1, then the numerator alone can be outputted 
        if self.den == 1:
            return str(self.num)
        # if the denominator is not equal to 1, then the numerator and denominator are to be outputted
        return str(self.num) + '/' + str(self.den)

    # returns a decimal value for the exact value of the fraction
    def eval(self):
        return self.num/self.den

p1 = Fraction(3, 5)
# p2 = Fraction(2, 7) 
# print(p1+p2) 
# print(p1/p2)
# print(3*p1, p1*3)
# print(p1/p2, p1/p2*-1)
# p1 += p2
# print(p1)
# p3 = Fraction(1, 5)
# p4 = Fraction(10, 25)
# print(p4)
# print()
# print(p3/p4) # 1/5 divided by 2/5
# # print(-1*p3/p4)