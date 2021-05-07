from integers_by_prime import *

class Fraction():
    def __init__(self, num, denom):
        self.num = Int_prime
        self.denom = Int_prime
    
    def __add__(self, other):
        denom = self.denom.lcm(other.denom)
        
    
    def __sub__(self, other):
        pass
    
    def __mul__(self, other):
        if (type(other) != Fraction):
            other = Fraction(other)
        num = self.num * other.num
        denom = self.denom * other.denom
        return Fraction(num, denom).reduce()
    
    def __truediv__(self, other):
        if (type(other) != Fraction):
            other = Fraction(other)
        num = self.num * other.denom
        denom = self.denom * other.num
        return Fraction(num, denom).reduce()
    
    def __eq__(self, other):
        if (type(other) == Fraction):
            return (self.num / other.num) == (self.denom / other.denom)
        else:
            return self.num / self.denom == other

    def __str__(self):
        return "{}/{}".format(self.num, self.denom)

    def reduce(self):
        if (self.denom < 0):
            self.num *= -1
            self.denom *= -1

        for i in range(min(abs(self.num), abs(self.denom)) // 2, 0, -1):
            if (self.num % i == 0 and self.denom % i == 0):
                return Fraction(self.num / i, self.denom / i)
        return self

    def inverse(self):
        return Fraction(self, denom, num)
