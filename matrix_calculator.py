from matrix_interface import *
from tkinter import *

class MatrixCalculator():

    def __init__(self, name):
        self.line = 0
        self.mi1 = None
        self.mi2 = None

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
        mi1 = MatrixInterface("matrix 1")

    def calculate(self, option):
        m1 = self.mi1.matrix
        m2 = self.mi2.matrix
        if self.operators == "RREF":
            # matrix1.matrix_display(this, line)
            pass

mc = MatrixCalculator("calculator")
mainloop()