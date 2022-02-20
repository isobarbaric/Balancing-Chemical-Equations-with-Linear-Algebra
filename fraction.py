import math 

class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        nBottom = (self.den*other.den)/math.gcd(self.den, other.den)
        nTop = self.num*(nBottom/self.den) + other.num*(nBottom/other.den)
        return Fraction(int(nTop), int(nBottom))

    def __mul__(self, other):
        nTop = self.num*other.num
        nBottom = self.den*other.den
        return Fraction(nTop, nBottom)

    def __repr__(self):
        return str(self.num) + '/' + str(self.den)

# p1 = Fraction(3, 5)
# p2 = Fraction(2, 7) 
# print(p1+p2) 
# print(p1*p2)

# class Reaction:

#     def __init__(self, ):
#         self. 