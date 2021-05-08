from matrix import *
from complex_numbers import *
from fractions import *
from tkinter import *

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


def set_size(width, height, gui):
    # convert from input boxes to ints
    width = int(width.get().strip())
    height = int(height.get().strip())

    matrix_inputs = [[None for i in range(height)] for ii in range(width)]
    for x in range(width):
        for y in range(height):
            matrix_inputs[x][y] = Entry(gui)
            matrix_inputs[x][y].grid(row=y+4, column=x)


def main():
    

    master = Tk()
    Label(master, text='rows').grid(row=0)
    Label(master, text='column').grid(row=1)
    ok = Button(master, text="ok", command=lambda: set_size(width, height, master))
    ok.grid(row=3)
    width = Entry(master)
    width.grid(row=0, column=1)
    height = Entry(master)
    height.grid(row=1, column=1)
    
    mainloop()
    

    



if __name__ == "__main__":
    main()