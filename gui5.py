from tkinter import *
from tkinter.ttk import Style, Label
root = Tk()
root.geometry("700x500")
root.config(bg='white')

top = Frame(root)
bottom = Frame(root, bg='white')
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

# create the widgets for the top part of the GUI,
# and lay them out
btn1 = Button(root, text="System", width=10, height=1)
btn2 = Button(root, text="Clear", width=10, height=1)
btn3 = Button(root, text="Clear", width=10, height=1)
btn1.pack(in_=top, side=LEFT, pady=10)
btn2.pack(in_=top, side=LEFT, pady=10)
btn3.pack(in_=top, side=LEFT, pady=10)

# create the widgets for the bottom part of the GUI,
# and lay them out
text = Text(root, width=35, height=15)
scrollbar = Scrollbar(root)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(in_=bottom, side=RIGHT, fill=BOTH)
text.pack(in_=bottom, side=LEFT, fill=BOTH, expand=True)
style = Style()
style.configure("BW.TLabel", foreground="black", background="white")

for i in range(100):

    lbl = Label(master=text, text="hi", style="BW.TLabel")
    lbl.pack(side=LEFT)



root.mainloop()