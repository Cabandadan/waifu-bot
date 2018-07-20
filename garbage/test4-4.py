# Attempted speech

#imports
from tkinter import *
import tkinter.messagebox
import random
import clever

#create the Window
root = Tk()
root.title("Test")
#root.geometry("500x500")
root.configure()


#user info
user = 'dUWbjEeJnrSlP3AS'
key = '1jS25GWhpyvDSjWS9ONC16XuS9hyQXGm'
client = clever.CleverBot(user=user, key=key)

q_pres = {'who is my waifu':'2b'

}
#key funciton
def click():
    entered_text=textentry.get()
    output.delete(0.0, END)

    try:
        response = q_pres[entered_text]
    except:
        txt = entered_text
        response = client.query(txt)
    output.insert(END, response)


#frames
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

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

#create acc
#requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'frost'})

#kick off the event loop
root.mainloop()
