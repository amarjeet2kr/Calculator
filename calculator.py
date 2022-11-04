from tkinter import *

root = Tk()
root.title("Calculator")
# root.iconbitmap("./images/calculator.ico")
root.geometry("340x450")
root.minsize(340, 450)
root.maxsize(340, 450)


def Quit_pgm():
    root.destroy()

#Open input box
e = Entry(root, width=27, bd=5, font=10)
e.grid(row=0, column=0, columnspan=4, padx=2, pady=10)
#End of input box

def Clear_result():
    e.delete(0, END)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def Button_addition():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)
    
def Button_substraction():
    first_number = e.get()
    global f_num
    global math
    math = "substract"
    f_num = float(first_number)
    e.delete(0, END)

def Button_multiplication():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = float(first_number)
    e.delete(0, END)

def button_division():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    e.delete(0, END)

def Result():
    second_number = e.get()
    e.delete(0, END)
    
    if math == "addition":
        result_added = round(f_num + float(second_number), 10)
        e.insert(0, result_added)

    if math == "substract":
        result_added = round(f_num - float(second_number), 10)
        e.insert(0, result_added)

    if math == "multiply":
        result_added = round(f_num * float(second_number), 10)
        e.insert(0, result_added)

    if math == "divide":
        result_added = round(f_num / float(second_number), 10)
        e.insert(0, result_added)


#Open Button 
button_7 = Button(root, text="7", padx=27, pady=20, font=18, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=27, pady=20, font=18, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=27, pady=20, font=18, command=lambda: button_click(9))
button_back_space = Button(root, text="Exit", padx=15, pady=20, font=10, command=Quit_pgm)

button_4 = Button(root, text="4", padx=27, pady=20, font=18, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=27, pady=20, font=18, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=27, pady=20, font=18, command=lambda: button_click(6))
button_divide = Button(root, text="/", padx=29, pady=20, font=18, command=button_division)

button_1 = Button(root, text="1", padx=27, pady=20, font=18, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=27, pady=20, font=18, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=27, pady=20, font=18, command=lambda: button_click(3))
button_multiply = Button(root, text="X", padx=25, pady=20, font=18, command=Button_multiplication)

button_point = Button(root, text=".", padx=30, pady=20, font=18, command=lambda: button_click("."))
button_0 = Button(root, text="0", padx=27, pady=20, font=18, command=lambda: button_click(0))
button_subtract = Button(root, text="-", padx=30, pady=20, font=18, command=Button_substraction)
button_add = Button(root, text="+", padx=26, pady=20, font=18, command=Button_addition)

button_result = Button(root, text="=", padx=69, pady=20, font=18, command=Result)
button_clear = Button(root, text="Clear", padx=50, pady=20, font=18, command=Clear_result)

#put the button on screen
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_back_space.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_point.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_result.grid(row=5, column=0, columnspan=2)
button_clear.grid(row=5, column=2, columnspan=2)
#Close of button

root.mainloop()