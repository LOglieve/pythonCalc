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
    index = 0
    count = 1

    while (index <= 8):
        if(count <= 3) :
            buttons.append(Button(row1, text=count, font = ("Verdana", 22), relief = GROOVE, border=0,command = btn_clicked(value=count)))
        elif(index >= 6):
            buttons.append(Button(row3, text=count, font = ("Verdana", 22), relief = GROOVE, border=0,command = btn_clicked(value=count)))
        else:
            buttons.append(Button(row2, text=count, font = ("Verdana", 22), relief = GROOVE, border=0,command = btn_clicked(value=count)))
        buttons[index].pack(side=LEFT,expand=True,fill='both')
        index +=1
        count +=1

main()