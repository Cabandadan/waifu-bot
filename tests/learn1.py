from tkinter import *

#initialize window
root = Tk()

#base info
root.title("Kirise Akane")
root.geometry('500x500')

#frames
#topFrame = Frame(root)
#topFrame.pack()
#bottomFrame = Frame(root)
#bottomFrame.pack(side=BOTTOM)
#rightFrame = Frame(root)
#rightFrame.pack(side=RIGHT)

#functions
def die():
    print("Bai!")
    exit()

def click():
    hola.configure(text="AHHHHHH")

#label widgets
spcr = Label(root, text="  ")
spcr2 = Label(root, text="  ")

hola = Label(root, text="Hola", font=("Times New Roman", 40))
hola.grid(column=0,row=0)

jola = Label(root, text="Jola")
jola.grid(column=1,row=3)

def changed():
    res = "welcome to " + txt.get()
    btn2.configure(text= res)
    txt.focus()

def disable():
    txt.configure(state='disabled')
def enable():
    txt.configure(state='normal')

btn = Button(root, text="Click to instantly die", command=die, bg="red")
btn2 = Button(root, text="Clicgreen", command=changed, bg="green")
btn.grid(column=1,row=4)
spcr2.grid(column=2,row=4)
btn2.grid(column=3,row=4)
spcr.grid(column=1, row=6)
btn = Button(root, text="Click to restore", command=click, fg="purple")
btn.grid(column=2,row=6)

txt = Entry(root,width=20)
txt.grid(column=3,row=7)
btn3 = Button(root, text="AAAAAAAAAAA", command=disable, fg="black")
btn3.grid(column=3,row=8)
btn3 = Button(root, text="enabledA", command=enable, fg="black")
btn3.grid(column=3,row=9)




#kicks off the main loop
root.mainloop()
