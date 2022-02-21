
from math import gcd

class Fraction:

    def __init__(self, num, den=1):
        self.num = num
        self.den = den

    def __add__(self, other):
        nBottom = (self.den*other.den)/gcd(self.den, other.den)
        nTop = self.num*(nBottom/self.den) + other.num*(nBottom/other.den)
        nTop /= gcd(int(nTop), int(nBottom))
        nBottom /= gcd(int(nTop), int(nBottom))
        return Fraction(int(nTop), int(nBottom))

    def __sub__(self, other):
        nBottom = (self.den*other.den)/gcd(self.den, other.den)
        nTop = (self.num*(nBottom/self.den) - other.num*(nBottom/other.den))
        nTop /= gcd(int(nTop), int(nBottom))
        nBottom /= gcd(int(nTop), int(nBottom))
        return Fraction(int(nTop), int(nBottom))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            nTop = self.num*other
            nBottom = self.den
        else:                
            nTop = self.num*other.num
            nBottom = self.den*other.den
        nTop /= gcd(int(nTop), int(nBottom))
        nBottom /= gcd(int(nTop), int(nBottom))
        if (nBottom < 0):
            nTop *= -1
            nBottom *= -1
        return Fraction(int(nTop), int(nBottom))

    def __rmul__(self, other): 
        return self.__mul__(other)

    def __truediv__(self, other):
        nTop = self.num*other.den
        nBottom = self.den*other.num
        nTop /= gcd(int(nTop), int(nBottom))
        nBottom /= gcd(int(nTop), int(nBottom))
        return Fraction(int(nTop), int(nBottom))

    def __repr__(self):
        if self.den == 1:
            return str(self.num)
        return str(self.num) + '/' + str(self.den)

    def __iadd__(self, other):
        return self.__add__(other)

p1 = Fraction(3, 5)
p2 = Fraction(2, 7) 
print(p1+p2) 
print(p1/p2)
print(3*p1, p1*3)
print(p1/p2, p1/p2*-1)
p1 += p2
print(p1)