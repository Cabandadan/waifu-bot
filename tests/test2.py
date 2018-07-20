#simple GUI

from tkinter import *

#create the Window
root = Tk()

#modify the Window
root.title("Kirise Akane")
root.geometry("500x500")
root.configure()

topFrame = Frame(root)
#frames
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#buttons
button1 = Button(bottomFrame, text="High Five", fg="white", bg="#373737")
button2 = Button(bottomFrame, text="Smile", fg="white", bg="#373737")
button3 = Button(bottomFrame, text="Pat", fg="white", bg="#373737")
button4 = Button(bottomFrame, text="Say hi", fg="white", bg="#373737")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

#textentry
textentry = Entry(root,width=20)
textentry.pack(side=BOTTOM)

#text
textinp = Label(root, text="Say something: ")
textinp.pack(side=BOTTOM)

#labels
blank = Label(topFrame, text="\n \n")
blank2 = Label(bottomFrame, text="\n \n \n \n")
blank.pack()
blank2.pack(side = BOTTOM)

#images
photo = PhotoImage(file="bw_test.png")
bw_test = Label(root, image=photo)
bw_test.pack(side=TOP)

#kick off the event loop (keeps continually on screen)
root.mainloop()
