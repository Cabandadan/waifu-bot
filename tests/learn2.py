from tkinter import *
from tkinter.ttk import *

#root
root = Tk()
root.title("UGh")
root.geometry('500x500')

combo = Combobox(root)
combo['values'] = (1,2,3,4,5, "Text")
combo.current(1)
combo.grid(column=0,row=0)

#chk_state = BooleanVar()
#chk_state.set(True) #set check state
chk_state = IntVar()

#chk_state.set(0) #uncheck

chk_state.set(1) #check
chk = Checkbutton(root, text='Choose', var=chk_state)
chk.grid(column=1, row=1)

root.mainloop()
