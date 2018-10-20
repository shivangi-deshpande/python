from tkinter import *
from gui8 import *

root = Tk()
root.geometry("700x500")
root.config(bg='white')

top = Frame(root)
bottom = Frame(root, bg='white')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

# create the widgets for the top part of the GUI,
# and lay them out
btn1 = Button(root, text="Enter", width=10, height=1)
btn2 = Button(root, text="Clear", width=10, height=1)
btn3 = Button(root, text="Clear", width=10, height=1)
btn1.pack(in_=top, side=LEFT)
btn2.pack(in_=top, side=LEFT)
btn3.pack(in_=top, side=LEFT)

# create the widgets for the bottom part of the GUI,
# and lay them out
# text = Text(root, width=35, height=15)
# scrollbar = Scrollbar(root)
# scrollbar.config(command=text.yview)
# text.config(yscrollcommand=scrollbar.set)
# scrollbar.pack(in_=bottom, side=RIGHT, fill=Y)
# text.pack(in_=bottom, side=LEFT, fill=BOTH, expand=True)

McListBox(bottom)




root.mainloop()