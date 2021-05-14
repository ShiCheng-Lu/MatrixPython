from matrix_interface import *
from tkinter import *

class MatrixCalculator():

    def __init__(self, name):
        self.line = 0
        self.mi1 = None
        self.mi2 = None
        self.op = None

        self.gui = Tk(className=name)

        options = ["RREF", "multiply"]
        self.operators = Listbox(self.gui)
        self.operators.grid(row=3, column=0)
        for option in options:
            self.operators.insert(END, option)


        self.confirm_button = Button(self.gui, text="confirm", command=self.take_input)
        self.confirm_button.grid(row=5, column=0)

        self.calculate_button = Button(self.gui, text="calculate", command=self.calculate)
        self.calculate_button.grid(row=5, column=1)
    
    def take_input(self):
        self.op = self.operators.get(ACTIVE)
        if self.op == "RREF":
            self.mi1 = MatrixInterface("matrix 1")
            
        elif self.op == "multiply":
            self.mi1 = MatrixInterface("matrix 1")
            self.mi2 = MatrixInterface("matrix 2")
        
        print(self.op)

    def calculate(self):
        print(self.op)
        if self.op == "RREF":
            m1 = self.mi1.matrix
            # matrix1.matrix_display(this, line)
            m1.rref()
            self.matrix_display(m1)
        elif self.op == "multiply":
            m1 = self.mi1.matrix
            m2 = self.mi2.matrix
            try:
                self.matrix_display(m1 * m2)
            except:
                print("error")
    
    def matrix_display(self, matrix):
        for x in range(matrix.col):
            for y in range(matrix.row):
                num = str(round(matrix.get(x, y), 5))
                Label(self.gui, text=num).grid(row=y+20, column=x)

mc = MatrixCalculator("calculator")
mainloop()