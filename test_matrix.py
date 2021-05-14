from matrix import *
from complex_numbers import *

def test_1():
    m = Matrix(3, 3)
    m.data = [  [Complex(1), Complex(2), Complex(3)],
                [Complex(4), Complex(5), Complex(6)],
                [Complex(7), Complex(8), Complex(10)]]
    
    print(m.rref())

    m.data = [  [Complex(1), Complex(2), Complex(3)],
                [Complex(4), Complex(5), Complex(6)],
                [Complex(7), Complex(8), Complex(10)]]
    print(m.inverse())


def main():
    test_1()

if __name__ == "__main__":
    main()