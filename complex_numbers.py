
# a module to handle complex number operations
class Complex():
    '''
    Complex(real, img) a representation for complex numbers

    C.real : num
        the real part of the Complex number
    
    C.img : num
        the imaginary part of the Complex number
    '''
    def __init__(self, real, img):
        super().__init__()
        self.real = real
        self.img = img

    def __mul__(self, other):
        real = self.real * other.real - self.img * other.img
        img = self.real * other.img + self.img * other.real
        return Complex(real, img)

    def __truediv__(self, other):
        num = self * other.conjugate()
        denom = other * other.conjugate()
        denom = denom.real
        return Complex(num.real / denom, num.img / denom)
    
    def __div__(self, other):
        return self.__truediv__(other)

    def __add__(self, other):
        real = self.real + other.real
        img = self.img + other.img
        return Complex(real, img)
    
    def __sub__(self, other):
        real = self.real - other.real
        img = self.img + other.img
        return Complex(real, img)
    
    def __eq__(self, other):
        if (type(other) == Complex):
            return self.real == other.real and self.img == other.img
        else:
            return self.real == other and self.img == 0

    def __str__(self):
        if (self.img == 0):
            return "{}".format(str(self.real))
        elif (self.img > 0):
            return "{}+{}i".format(str(self.real), str(self.img))
        else:
            return "{}{}i".format(str(self.real), str(self.img))
    
    def __round__(self, ndigits):
        return Complex(round(self.real, ndigits), round(self.img, ndigits))
    '''
    C.conjugate()
    return the conjugate of the complex number
    '''
    def conjugate(self):
        return Complex(self.real, self.img * -1)
    
    def invert(self):
        return Complex(1, 0) / self
