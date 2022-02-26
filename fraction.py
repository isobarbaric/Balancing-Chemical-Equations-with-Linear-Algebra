
import math 

class Fraction:
    '''
        Stores all of the relevant functionality needed to model fractions
    '''

    # initializing a Fraction object with default denominator being 1
    def __init__(self, num, den = 1):
        '''
            :param num: numerator of the fraction being initialized
            :param den: denominator of the fraction being initialized
            Returns a Fraction object
        '''

        # this assertion prevents an undefined fraction from being initialized 
        assert den != 0

        # simplification to simplest form
        self.num = int(num/math.gcd(num, den))
        self.den = int(den/math.gcd(den, num))

    def __add__(self, other):
        '''
            :param other: a Fraction object to be added to the current Fraction object
            Overloads the addition operator for Fraction class
        '''
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

    def __sub__(self, other):
        '''
            :param other: a Fraction object to be subtracted from the current Fraction object
            Overloads the subtraction operator for Fraction class
        '''
        return self.__add__(-1*other)


    def __mul__(self, other):
        '''
            :param other: an integer or Fraction to be multiplied with the current Fraction object
            Overloads the multiplication operator for Fraction class
        '''
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


    def __rmul__(self, other): 
        '''
            :param other: an integer Fraction object to be added to the current Fraction object
            Builds on top of the multiplication operator for fractions so that multiplication can occur both with integers in front and integers after a fraction object
        '''
        return self.__mul__(other)

    def __truediv__(self, other):
        '''
            :param other: an integer or Fraction to be multiplied with the current Fraction object
            Overloads the division operator for Fraction class
        '''
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

    def __repr__(self):
        '''
            Defines how a fraction is to be printed 
        '''

        # if the denominator is equal to 1, then the numerator alone can be outputted 
        if self.den == 1:
            return str(self.num)
        # if the denominator is not equal to 1, then the numerator and denominator are to be outputted
        return str(self.num) + '/' + str(self.den)

    # returns a decimal value for the exact value of the fraction
    def eval(self):        
        '''
            Returns the numerical value of the current Fraction object
        '''
        return self.num/self.den