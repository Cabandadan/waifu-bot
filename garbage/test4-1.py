#simple GUI

from tkinter import *

#key down funciton
def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_dict[entered_text]
    except:
        definition = "sorry senpai, i'm not smart enough to respond to that yet"
    output.insert(END, definition)

#create the Window
root = Tk()

#modify the Window
root.title("Kirise Akane")
#root.geometry("500x500")
root.configure()

#frames
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)

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
textoutp = Label(bottomFrame,text="Kirise: ",font="none 10 bold")
textoutp.pack(side=BOTTOM)

#images
photo = PhotoImage(file="bw_test.png")
bw_test = Label(root, image=photo)
bw_test.pack(side=TOP)

#dictionary
my_dict = {
'hi' : 'hello', 'who is my waifu?' : '2b','how is your day?' : 'it is a wonderful day senpai!'
}

'''
#exitfunc
def close_window():
    root.destroy()
    exit()

#exitbutton
exitbutton = Button(root, text="KiLlmE",command=close_window)
exitbutton.pack(side=BOTTOM)
'''

#kick off the event loop (keeps continually on screen)
root.mainloop()
