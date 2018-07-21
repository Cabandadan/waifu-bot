#imports
from tkinter import *
import tkinter.messagebox
import random
import requests
import json

#create the Window
root = Tk()

#modify the Window
root.title("Test")
#root.geometry("500x500")
root.configure()

user = 'dUWbjEeJnrSlP3AS'
key = '1jS25GWhpyvDSjWS9ONC16XuS9hyQXGm'
requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'frost'})

#key down function
def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        response = q_pres[entered_text]
    except:
        txt = entered_text
        r= json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'frost', 'text':txt}).text)
        response = r['response']
    output.insert(END, response)


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
photo0 = PhotoImage(file="tests/2.png")
bw_test0 = Label(topFrame, image=photo0)
bw_test0.image = photo0
bw_test0.pack(side=TOP)

photo = PhotoImage(file="tests/1.png")
bw_test = Label(topFrame, image=photo)
bw_test.image = photo
#bw_test.pack(side=TOP)

send = Button(bottomFrame,text="Send!",width=5,command=click)
textentry = Entry(root,width=30)
textinp = Label(root, text="Say something:")
blank = Label(topFrame, text="")
blank2 = Label(bottomFrame, text="")
output = Text(bottomFrame, width=60,height=5,wrap=WORD)
textoutp = Label(bottomFrame,text="Respone: ",font="none 10 bold")

photo2 = PhotoImage(file="tests/3.png")
bw_test2 = Label(topFrame, image=photo2)
bw_test2.image = photo2

send2 = Button(bottomFrame,text="Sefdsnd!",width=5,command=click)
textinp2 = Label(root, text="Say somegfdgfdsthing:")
textoutp2 = Label(bottomFrame,text="Answfffffffer: ",font="none 10 bold")

def forget():
    textentry.forget()
    bw_test.forget()
    textoutp.forget()
    blank.forget()
    output.forget()
    blank2.forget()
    textinp.forget()
    send.forget()
    send2.forget()
    textinp2.forget()
    textoutp2.forget()
    bw_test2.forget()
    bw_test0.forget()

#exitfunc
def close_window():
    root.destroy()
    exit()

def test0():
    forget()
    bw_test0.pack(side=TOP)

def test1():
    forget()
    #submitbutton
    #send = Button(bottomFrame,text="Send!",width=5,command=click)
    send.pack()

    #textentry
    #textentry = Entry(root,width=30)
    textentry.pack(side=BOTTOM)

    #text
    #textinp = Label(root, text="Say something:")
    textinp.pack(side=BOTTOM)

    #blanks
    #blank = Label(topFrame, text="")
    #blank2 = Label(bottomFrame, text="")
    blank.pack()
    blank2.pack(side = BOTTOM)

    #outputbox
    #output = Text(bottomFrame, width=60,height=5,wrap=WORD)
    output.pack(side=BOTTOM)

    #respone
    #textoutp = Label(bottomFrame,text="Answer: ",font="none 10 bold")
    textoutp.pack(side=BOTTOM)

    #images
    bw_test.pack(side=TOP)

def test2():
    forget()
    #submitbutton
    #send = Button(bottomFrame,text="Send!",width=5,command=click)
    send2.pack()
    #textentry
    #textentry = Entry(root,width=30)


    #text
    #textinp = Label(root, text="Say something:")
    textinp2.pack(side=BOTTOM)

    #blanks
    #blank = Label(topFrame, text="")
    #blank2 = Label(bottomFrame, text="")
    blank.pack()
    blank2.pack(side = BOTTOM)

    #outputbox
    #output = Text(bottomFrame, width=60,height=5,wrap=WORD)
    output.pack(side=BOTTOM)

    #respone
    #textoutp = Label(bottomFrame,text="Answer: ",font="none 10 bold")
    textoutp2.pack(side=BOTTOM)

    #images
    bw_test2.pack(side=TOP)

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
layoutMenu.add_command(label="Default", command=test0)
layoutMenu.add_command(label="Layout 1", command=test1)
layoutMenu.add_command(label="Layout 2", command=test2)



#setup_layout()

#kick off the event loop (keeps continually on screen)
root.mainloop()
