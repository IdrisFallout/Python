from tkinter import *

root = Tk()
# root.geometry('293x432')
root.resizable(False, False)

back_color = "dark orange"
font1 = ('Montserrat', 9)
root.configure()
# root.iconbitmap("logo.ico")

def buttonClick(number):
    current = e.get()
    buttonClear()
    e.insert(0, str(current) + str(number))

def buttonClear():
    e.delete(0, END)

def buttonAdd():
    first_num = e.get()
    try:
        global operation
        operation = 'addition'
        global f_num
        f_num = float(first_num)
        buttonClear()
    except:
        buttonClear()
        e.insert(0, "SYNTAX ERROR")

def buttonSubtract():
    try:
        first_num = e.get()
        global operation
        operation = 'subtraction'
        global fs_num
        fs_num = float(first_num)
        buttonClear()
    except:
        buttonClear()
        e.insert(0, "SYNTAX ERROR")

def buttonMultiply():
    try:
        first_num = e.get()
        global operation
        operation = 'multiplication'
        global fm_num
        fm_num = float(first_num)
        buttonClear()
    except:
        buttonClear()
        e.insert(0, "SYNTAX ERROR")

def buttonDivide():
    try:
        first_num = e.get()
        global operation
        operation = 'division'
        global fd_num
        fd_num = float(first_num)
        buttonClear()
    except:
        buttonClear()
        e.insert(0, "SYNTAX ERROR")

def buttonResult():
    if operation == 'addition':
        try:
            second_num = e.get()
            buttonClear()
            e.insert(0, float(float(f_num) + float(second_num)))
        except:
            buttonClear()
            e.insert(0, "SYNTAX ERROR")

    if operation == 'subtraction':
        try:
            second_num = e.get()
            buttonClear()
            e.insert(0, float(float(fs_num) - float(second_num)))
        except:
            buttonClear()
            e.insert(0, "SYNTAX ERROR")

    if operation == 'multiplication':
        try:
            second_num = e.get()
            buttonClear()
            e.insert(0, float(float(fm_num) * float(second_num)))
        except:
            buttonClear()
            e.insert(0, "SYNTAX ERROR")

    if operation == 'division':
        try:
            second_num = e.get()
            buttonClear()
            e.insert(0, float(float(fd_num) / float(second_num)))
        except:
            buttonClear()
            e.insert(0, "ERROR")

root.title("CALCULATOR")
e = Entry(root, borderwidth=5, width=35, font=('Montserrat ExtraBold', 9))
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# create buttons
button1 = Button(root, text="1", padx=40, pady=20, font=font1, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, font=font1, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, font=font1, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, font=font1, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, font=font1, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, font=font1, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, font=font1, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, font=font1, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, font=font1, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=40, pady=20, font=font1, command=lambda: buttonClick(0))

button_add = Button(root, text="+", padx=39, pady=20, font=font1, command=buttonAdd)
button_equal = Button(root, text="=", padx=91, pady=20, font=font1, command=lambda: buttonResult())
button_clear = Button(root, text="Clear", padx=79, pady=20, font=font1, command=buttonClear)

button_subtract = Button(root, text="-", padx=40, pady=20, font=font1, command=buttonSubtract)
button_multiply = Button(root, text="x", padx=40, pady=20, font=font1, command=buttonMultiply)
button_divide = Button(root, text="/", padx=41, pady=20, font=font1, command=buttonDivide)

# display buttons
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

button_add.grid(row=4, column=1)
button_equal.grid(row=6, column=1, columnspan=2)
button_clear.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=6, column=0)


root.mainloop()