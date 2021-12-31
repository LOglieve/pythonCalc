from tkinter import *

calc = ""
buttonsInt = []
buttonsOp = []
A = 0
operator = ''
result = 0

count = [1,2,3,4,5,6,7,8,9,]
opers = ['+', '-', 'X', 'C', '<-', '=', '/']

def btn_clicked(value):
    global calc
    global A
    global opers

    if value == '=':
        if(operator == '+'):
            #temp
            result = A
    if value in opers:
        A = int(calc)
        calc = calc + ' ' + value + ' '
    else:
        calc = calc + str(value)
    data.set(calc)

def addButtons():
    global count
    global opers
    for i in count:
        def func (x=i):
            return btn_clicked(x)

        if(i <= 3) :
            buttonsInt.append(Button(row1, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        elif(i >= 7):
            buttonsInt.append(Button(row3, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        else:
            buttonsInt.append(Button(row2, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        buttonsInt[i-1].pack(side=LEFT,expand=True,fill='both')

    index = 0
    for i in opers:
        def func(x=i):
            return btn_clicked(x)
        print(i)
        if (i == '+'):
            buttonsOp.append(Button(row1, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        elif (i == '-'):
            buttonsOp.append(Button(row2, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        elif (i == 'X'):
            buttonsOp.append(Button(row3, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        else:
            buttonsOp.append(Button(row4, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        buttonsOp[index].pack(side=LEFT,expand=True,fill='both')
        index +=1
#----------------------------------------------------------------------------------------------------------------------------------------------
#                                                      MAIN CODE
#----------------------------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

data = StringVar()
label = Label(root, text="Label", anchor=SE, font = ("Verdana",20), textvariable=data, background='#ffffff', fg="#000000")
label.pack(expand=True,fill="both")

row1 = Frame(root, bg="#ffffff")
row1.pack(expand=True,fill="both")
row2 = Frame(root, bg="#ffffff")
row2.pack(expand=True,fill="both")
row3 = Frame(root, bg="#ffffff")
row3.pack(expand=True,fill="both")
row4 = Frame(root, bg="#ffffff")
row4.pack(expand=True,fill="both")

addButtons()

root.mainloop()


