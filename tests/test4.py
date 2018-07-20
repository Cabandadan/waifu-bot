#simple GUI
from tkinter import *
import tkinter.messagebox

#create the Window
root = Tk()

#modify the Window
root.title("Test")
#root.geometry("500x500")
root.configure()

#key down funciton
def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_dict[entered_text]
    except:
        definition = "sorry senpai, i'm not smart enough to respond to that yet"
    output.insert(END, definition)

#frames
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)

#dictionary
my_dict = {
'hi' : 'hello', 'who is my waifu?' : '2b','how is your day?' : 'it is a wonderful day senpai!'
}

#images
photo = PhotoImage(file="tests/test5.png")
bw_test = Label(topFrame, image=photo)
bw_test.image = photo
bw_test.pack(side=TOP)

#exitfunc
def close_window():
    root.destroy()
    exit()

def test1():
    #submitbutton
    send = Button(bottomFrame,text="Send!",width=5,command=click)
    send.pack()

    #textentry
    textentry = Entry(root,width=30)
    textentry.pack(side=BOTTOM)

    #text
    textinp = Label(root, text="Say something:")
    textinp.pack(side=BOTTOM)

    #blanks
    blank = Label(topFrame, text="")
    blank2 = Label(bottomFrame, text="")
    blank.pack()
    blank2.pack(side = BOTTOM)

    #outputbox
    output = Text(bottomFrame, width=60,height=5,wrap=WORD)
    output.pack(side=BOTTOM)

    #respone
    textoutp = Label(bottomFrame,text="Answer: ",font="none 10 bold")
    textoutp.pack(side=BOTTOM)

    #images
    bw_test.pack(side=TOP)

def msgbox():
    tkinter.messagebox.showinfo('Hey!', 'There is nothing about me! :D')

#menus
menu = Menu(root)
root.config(menu=menu)

infoMenu = Menu(menu)
menu.add_cascade(label="Info", menu=infoMenu)
infoMenu.add_command(label="About", command=msgbox)
infoMenu.add_separator()
infoMenu.add_command(label="Exit", command=close_window)

layoutMenu = Menu(menu)
menu.add_cascade(label="Layout", menu=layoutMenu)
layoutMenu.add_command(label="Layout 1", command=test1)



#setup_layout()

#kick off the event loop (keeps continually on screen)
root.mainloop()
