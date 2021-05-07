from complex_numbers import *
from fractions import *

class Matrix():

    def __init__(self, row, column):
        super().__init__()
        self.row_len = row
        self.col_len = column
        self.data = [[0 for x in column] for y in row]

    def __str__(self):
        result_str = ""
        for row in range(self.row_len):
            for col in range(self.col_len):
                result_str += "{} ".format(str(self.data[row][col]))
            result_str += "\n"
        return result_str

    def __mul__(self, other):
        if (type(other) == Matrix):
            assert (self.col_len == other.row_len)
            result = Matrix(self.row_len, other.col_len)

            data = [[0 for x in other.col_len] for y in self.row_len]
            for row in range(self.row_len):
                for col in range(other.col_len):
                    # result is the sum of dot multiply between self (row) and other (column)
                    for i in range(1, self.col_len):
                        data[row][col] += self.data[row][i] * other.data[i][col]
            return result
        
        else:
            for row in range(self.row_len):
                for col in range(self.col_len):
                    self.data[row][col] *= other
            return self
    
    '''
    swap row1 and row2
    '''
    def ero1(self, row1, row2):
        assert(row1 <= self.row_len)
        assert(row1 > 0)
        assert(row2 <= self.row_len)
        assert(row2 > 0)
        assert(row1 != row2)

        data[row1], data[row2] = data[row2], data[row1] 

    def ero2(self, row, scale):
        assert(row <= self.row_len)
        assert(row > 0)

        for col in range(self.col_len):
            self.data[row][col] *= scale
    
    def ero3(self, row1, row2, scale):
        assert(row1 <= self.row_len)
        assert(row1 > 0)
        assert(row2 <= self.row_len)
        assert(row2 > 0)
        assert(row1 != row2)

        for col in range(self.col_len):
            self.data[row1][col] += self.data[row2][col] * scale

    
    '''
    M.print_row(row)
    print a row of the matrix
    '''
    def print_row(self, row):
        output_str = ""
        for i in range(self.col_len):
            output_str += "{} ".format(self.data[row][i])
        print("(" + output_str + ")")
    
    def rref(self):
        # to REF
        current_row = 0
        for pivot in range(self.col_len):
            #find the first row that doesn't start with 0
            for i in range(current_row, self.row_len):
                if (self.data[i][pivot] != 0):
                    # found a pivot
                    self.ero1(i, current_row)
                    self.ero2(current_row, self.data[current_row][pivot].invert())
                    self.print_row(current_row)
                    break
            else:
                # no pivot for this column, skip to next column
                continue

            # scale everything else to 0
            for i in range(0, self.row_len):
                if (i != current_row):
                    scale_factor = self.data[i][pivot] / self.data[current_row][pivot]

                    for col in range(pivot, self.col_len):
                        self.data[i][col] = self.data[i][col] - self.data[current_row][col] * scale_factor
            current_row += 1
        
        # to RREF
    

def str_to_complex_frac(string):
    if ("i" in string):
        pos = 1
        #something
        if (string.startswith("-")):
            string = string.strip("-")
            pos = -1
        #split into real and imaginary
        if ("+" in string):
            r_i = string.split("+")
        else:
            r_i = string.split("-")
        # real part
        if ("/" in r_i[0]):
            n = r_i[0].split("/")
            real = Fraction(int(n[0]) * pos, int(n[1]))
        else:
            real = Fraction(int(r_i[0]) * pos)
        # imaginary part
        if ("/" in r_i[1]):
            n = r_i[1].split("/")
            img = Fraction(int(n[0]) * pos, int(n[1]))
        else:
            img = Fraction(int(r_i[1]) * pos)
    else:
        if ("/" in string):
            n = string.split("/")
            real = Fraction(int(n[0]), int(n[1]))
        else:
            real = Fraction(int(string))
        img = 0
    
    return Complex(real, img)
            


def input_matrix():
    data = []
    row = input()
    while (row != ''):
        row_data = []
        for num in row.split(" "):
            row_data.append(str_to_complex_frac(num))
        data.append(row_data)
        row = input()
    return Matrix(data)


a = input_matrix()
b = input_matrix()

print(a * b)