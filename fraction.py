
import math 

class Fraction:

    # constructor
    def __init__(self, num, den = 1):
        # this assertion prevents an undefined fraction from being initialized 
        assert den != 0

        # simplification to simplest form
        self.num = int(num/math.gcd(num, den))
        self.den = int(den/math.gcd(den, num))

    # supporting the addition operation between Fraction objects
    def __add__(self, other):
        # determining the numerator and denominator for the new fraction        
        nBottom = (self.den*other.den)/math.gcd(self.den, other.den)
        nTop = self.num*(nBottom/self.den) + other.num*(nBottom/other.den)

        # if the numerator is 0, the entire fraction is effectively 0, regardless of what value the denominator has
        if (nTop == 0):
            return Fraction(0)

        # simplification to simplest form
        gcd_2 = math.gcd(int(nTop), int(nBottom))
        nTop /= gcd_2
        nBottom /= gcd_2

        # only one of the numerator and the denominator must contain a negative sign
        if (nBottom < 0):
            nTop *= -1
            nBottom *= -1

        return Fraction(int(nTop), int(nBottom))

    # supporting the subtraction operation between Fraction objects
    def __sub__(self, other):
        return self.__add__(-1*other)

    # supporting the multiplication operation between Fraction objects (first order)
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
        gcd_2 = math.gcd(int(nTop), int(nBottom))
        nTop /= gcd_2
        nBottom /= gcd_2

        # only one of the numerator and the denominator must contain a negative sign
        if (nBottom < 0):
            nTop *= -1
            nBottom *= -1

        return Fraction(int(nTop), int(nBottom))

    # supporting the multiplication operation between Fraction objects (second order)
    def __rmul__(self, other): 
        return self.__mul__(other)

    # supporting the division operation between Fraction objects
    def __truediv__(self, other):
        # determines the numerator and denominator for the new fraction
        nTop = self.num*other.den
        nBottom = self.den*other.num
 
        # if the numerator is 0, the entire fraction is effectively 0, regardless of what value the denominator has
        if (nTop == 0):
            return Fraction(0)

        # simplification to simplest form
        gcd_2 = math.gcd(int(nTop), int(nBottom))
        nTop /= gcd_2
        nBottom /= gcd_2

        # only one of the numerator and the denominator must contain a negative sign
        if (nBottom < 0):
            nTop *= -1
            nBottom *= -1

        return Fraction(int(nTop), int(nBottom))

    # creating a custom representation for Fraction objects
    def __repr__(self):
        # if the denominator is equal to 1, then the numerator alone can be outputted 
        if self.den == 1:
            return str(self.num)

        # if the denominator is not equal to 1, then the numerator and denominator are to be outputted
        return str(self.num) + '/' + str(self.den)

    # returns a decimal value for the exact value of the fraction
    def eval(self):        
        return self.num/self.den