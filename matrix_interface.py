from matrix import *
from complex_numbers import *
from fractions import *
from tkinter import *

class MatrixInterface():

    def __init__(self, name):
        self.width = 0
        self.height = 0
        self.matrix = Matrix(0, 0)
        self.matrix_inputs = [[]]

        self.gui = Tk(className=name)

        Label(self.gui, text='rows').grid(row=0)
        self.width_input = Spinbox(self.gui, from_=1, to=20, width=3)
        self.width_input.grid(row=1, column=1)
        self.width_input.delete(0)
        self.width_input.insert(0, "3")

        Label(self.gui, text='column').grid(row=1)
        self.height_input = Spinbox(self.gui, from_=1, to=20, width=3)
        self.height_input.grid(row=0, column=1)
        self.height_input.delete(0)
        self.height_input.insert(0, "3")

        self.set_size_button = Button(self.gui, text="ok", command=self.update)
        self.set_size_button.grid(row=3, column=0)

        self.confirm_button = Button(self.gui, text="confirm", command=self.create_matrix)
        self.confirm_button.grid(row=5, column=0)

        self.clear_button = Button(self.gui, text="clear", command=self.clear_inputs)
        self.clear_button.grid(row=5, column=1)

        self.display_button = Button(self.gui, text="display", command=self.matrix_display)
        self.display_button.grid(row=5, column=2)
        
        self.update()
    
    def set_size(self):
        # convert from input boxes to ints
        self.matrix_inputs = [[None for i in range(self.height)] for ii in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                self.matrix_inputs[x][y] = Entry(self.gui, width=12)
                self.matrix_inputs[x][y].grid(row=y+4, column=x)
        
        self.confirm_button.grid(row=5 + y, column=0)
        self.clear_button.grid(row=5 + y, column=1)
        self.display_button.grid(row=5 + y, column=2)

    def clear_inputs(self):
        for x in range(self.width):
            for y in range(self.height):
                self.matrix_inputs[x][y].delete(0, END)
    
    def clear_all(self):
        for x in range(self.width):
            for y in range(self.height):
                self.matrix_inputs[x][y].destroy()

    def update(self):
        self.clear_all()
        # clear then update all
        self.width = int(self.width_input.get())
        self.height = int(self.height_input.get())
        # re-set size
        self.set_size()
    
    def create_matrix(self):
        self.matrix = Matrix(self.height, self.width)
        for x in range(self.width):
            for y in range(self.height):
                value = str_to_complex(self.matrix_inputs[x][y].get())
                self.matrix.set(x, y, value)
    
    def matrix_display(self):
        for x in range(self.width):
            for y in range(self.height):
                num = str(round(self.matrix.get(x, y), 5))
                Label(self.gui, text=num).grid(row=y+20, column=x)

def str_to_complex(string):
    if string == "":
        return Complex(0, 0)
    string = string.replace(" ", "")

    real = 1
    if (string.startswith("-")):
        string = string.strip("-")
        real = -1
    
    img = 1
    if "-" in string:
        string = string.split("-")
        img = -1
    else:
        string = string.split("+")
    
    real *= float(string[0])
    if len(string) == 2:
        img *= float(string[1])
    else:
        img = 0

    return Complex(real, img)



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

def main():
    mi = MatrixInterface("matrix 1")
    mainloop()

if __name__ == "__main__":
    main()