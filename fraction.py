
from math import gcd

class Fraction:

    def __init__(self, num, den=1):
        assert den != 0
        self.num = int(num/gcd(num, den))
        self.den = int(den/gcd(den, num))

    def __add__(self, other):
        nBottom = (self.den*other.den)/gcd(self.den, other.den)
        nTop = self.num*(nBottom/self.den) + other.num*(nBottom/other.den)
        if (nTop == 0):
            return Fraction(0)
        gcd_2 = gcd(int(nTop), int(nBottom))
        nTop /= gcd_2
        nBottom /= gcd_2
        if (nBottom < 0):
            nTop *= -1
            nBottom *= -1
        return Fraction(int(nTop), int(nBottom))

    def __sub__(self, other):
        nBottom = (self.den*other.den)/gcd(self.den, other.den)
        nTop = (self.num*(nBottom/self.den) - other.num*(nBottom/other.den))
        if (nTop == 0):
            return Fraction(0)
        gcd_2 = gcd(int(nTop), int(nBottom))
        nTop /= gcd_2
        nBottom /= gcd_2
        if (nBottom < 0):
            nTop *= -1
            nBottom *= -1
        return Fraction(int(nTop), int(nBottom))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            nTop = self.num*other
            nBottom = self.den
        else:                
            nTop = self.num*other.num
            nBottom = self.den*other.den
        if (nTop == 0):
            return Fraction(0)
        gcd_2 = gcd(int(nTop), int(nBottom))
        nTop /= gcd_2
        nBottom /= gcd_2
        if (nBottom < 0):
            nTop *= -1
            nBottom *= -1
        return Fraction(int(nTop), int(nBottom))

    def __rmul__(self, other): 
        return self.__mul__(other)

    def __truediv__(self, other):
        nTop = self.num*other.den
        nBottom = self.den*other.num
        if (nTop == 0):
            return Fraction(0)
        gcd_2 = gcd(int(nTop), int(nBottom))
        nTop /= gcd_2
        nBottom /= gcd_2
        if (nBottom < 0):
            nTop *= -1
            nBottom *= -1
        return Fraction(int(nTop), int(nBottom))

    def __repr__(self):
        if self.den == 1:
            return str(self.num)
        return str(self.num) + '/' + str(self.den)

    def __iadd__(self, other):
        return self.__add__(other)

    def __gt__(self, other):
        c1 = self.den*(self.den*other.den)
        c2 = other.den*(self.den*other.den)
        if (c1 > c2):
            return True
        return False

    def evl(self):
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