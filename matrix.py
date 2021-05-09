class Matrix():
    '''
    Matrix(row : int, column : int)

    create a (row)x(column) matrix
    
    Attributes
    ==========
    row : int
        the number of rows this Matrix has
    col : int
        the number of columns this Matrix has
    data : list of list
        the data contained in the Matrix
        data[x][y] is the x-y-th entry of the Matrix
    '''
    def __init__(self, row, column):
        super().__init__()
        self.row = row
        self.col = column
        self.data = [[0 for x in range(column)] for y in range(row)]

    def __str__(self):
        result_str = ""
        for row in range(self.row):
            for col in range(self.col):
                result_str += "{} ".format(str(self.data[row][col]))
            result_str += "\n"
        return result_str

    def __mul__(self, other):
        if (type(other) == Matrix):
            assert (self.col_len == other.row_len)
            result = Matrix(self.row, other.col_len)

            data = [[0 for x in other.col_len] for y in self.row]
            for row in range(self.row):
                for col in range(other.col_len):
                    # result is the sum of dot multiply between self (row) and other (column)
                    for i in range(1, self.col):
                        data[row][col] += self.data[row][i] * other.data[i][col]
            self = result
            return result
        
        else:
            for row in range(self.row):
                for col in range(self.col):
                    self.data[row][col] *= other
            return self
    
    def get(self, x, y):
        return self.data[y][x]

    def set(self, x, y, value):
        self.data[y][x] = value
    
    def ero1(self, row1, row2):
        '''
        M.ero1(row1 : int, row2 : int)
        swap row1 and row2
        '''
        # assert((row1 > 0) and (row1 <= self.row_len))
        # assert((row2 > 0) and (row2 <= self.row_len))
        # assert(row1 != row2)

        self.data[row1], self.data[row2] = self.data[row2], self.data[row1] 

    def ero2(self, row, scale):
        '''
        M.ero2(row1 : int, scale : num)
        scale row1 by a scale factor
        '''
        # assert(row <= self.row_len)
        # assert(row > 0)

        for col in range(self.col):
            self.data[row][col] *= scale
    
    def ero3(self, row1, row2, scale):
        '''
        M.ero3(row1 : int, row2 : int, scale : num)
        add to row1 by a scaled value of row2
        '''
        # assert((row1 > 0) and (row1 <= self.row_len))
        # assert((row2 > 0) and (row2 <= self.row_len))
        # assert(row1 != row2)

        for col in range(self.col):
            self.data[row1][col] += self.data[row2][col] * scale

    
    
    def print_row(self, row):
        '''
        M.print_row(row)
        print a row of the matrix
        '''
        output_str = ""
        for i in range(self.col):
            output_str += "{} ".format(self.data[row][i])
        print("(" + output_str + ")")
    
    def rref(self):
        # to REF
        current_row = 0
        for pivot in range(self.col):
            #find the first row that doesn't start with 0
            for i in range(current_row, self.row):
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
            for i in range(0, self.row):
                if (i != current_row):
                    scale_factor = self.data[i][pivot] / self.data[current_row][pivot]

                    for col in range(pivot, self.col):
                        self.data[i][col] = self.data[i][col] - self.data[current_row][col] * scale_factor
            current_row += 1
        
        # to RREF