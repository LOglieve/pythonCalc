from tkinter import *

# Buttons
buttonsInt = []
buttonsOp = []

bodmas = ['/', '*', '+', '-']

calc = []

A = 0
B = 0

operator = ''
result = 0

count = [1,2,3,4,5,6,7,8,9,0]
opers = ['+', '-', '*', 'C', '<-', '=', '/', '.']

# OPERATIONS
def add(x, y):
    return float(x) + float(y)

def subtract(x, y):
    return float(x) - float(y)

def multiply(x, y):
    return float(x) * float(y)

def divide(x, y):
    return float(x) / float(y)

def equals():
    global calc
    global bodmas
    # print('in here :)')

    for x in bodmas:
        # print('hello')
        i = 0
        while i < len(calc):
            # print('hi' + str(len(calc)))
            if(calc[i] == x):
                
                if(x == '/'):
                    calc[i-1] = str(divide(calc[i-1], calc[i+1]))
                    print(calc)
                elif(x == '*'):
                      calc[i-1] = str(multiply(calc[i-1], calc[i+1]))
                      print(calc)
                elif(x == '+'):
                      calc[i-1] = str(add(calc[i-1], calc[i+1]))
                      print(calc)
                elif(x == '-'):
                      calc[i-1] = str(subtract(calc[i-1], calc[i+1]))
                      print(calc)
                del(calc[i+1])
                del(calc[i])
                i = i - 2

            i = i + 1
                

# Button clicked
def btn_clicked(value):
    global calc
    global A
    global opers
    delim = ' '

    value = str(value)
    
    if value == '=':
        equals()
    elif value == 'C':
        calc = []
    elif value == '<-':
        if len(calc) > 0:
            if len(calc[-1]) == 1:
                del(calc[-1])
            else:
                temp = calc[-1]
                temp = temp[:-1]
                calc[-1] = temp
    elif value == '.':
        if calc[-1] not in opers:
            calc[-1] = calc[-1] + value
    else:
        if len(calc) == 0:
            # print('here 1')
            calc.append(value)
        elif calc[-1] in opers:
            # print('here 2')
            calc.append(value)
        elif value in opers:
            # print('here 3')
            calc.append(value)
        else:
            # print('here 4')
            calc[-1] = calc[-1] + value

    data.set(delim.join(calc))

# create all buttons
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
        # print(i)
        if (i == '+'):
            buttonsOp.append(Button(row1, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        elif (i == '-'):
            buttonsOp.append(Button(row2, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        elif (i == '*'):
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


