from tkinter import *

calc = ""
buttons = []

def main() :
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

    addButtons(row1, row2, row3)

    root.mainloop()

def btn_clicked(value):
    print(value)

def addButtons(row1, row2, row3):
    count = [1,2,3,4,5,6,7,8,9]
    

    for i in count:
        def func (x=i):
            return btn_clicked(x)

        if(i <= 3) :
            buttons.append(Button(row1, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        elif(i >= 7):
            buttons.append(Button(row3, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        else:
            buttons.append(Button(row2, text=i, font = ("Verdana", 22), relief = GROOVE, border=0, command = func))
        buttons[i-1].pack(side=LEFT,expand=True,fill='both')

main()