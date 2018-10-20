from tkinter import *
from tkinter import ttk

root = Tk()
root.minsize(width=500, height=600)
root.config(bg='white')
root.wm_title("System Monitor")

single = Frame(root)
single.configure(bg="black")
tree = ttk.Treeview(single)

tree["columns"]= "one"
tree.column("one", width=100)
# tree = ttk.Treeview(columns=process_header, show="headings")
vsb = ttk.Scrollbar(orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(orient="horizontal",command=tree.xview)
tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew', in_=single)
vsb.grid(column=1, row=0, sticky='ns', in_=single)
hsb.grid(column=0, row=1, sticky='ew', in_=single)

vsb.pack()
hsb.pack()



# id1 = tree.insert("" , 0,    text="Line 1", values=("1A"))
# tree.insert("" , "end",values=("1A"))
for i in range(100):
    tree.insert("", "end",text=" "+str(i), values=("A "+str(i)))

# tree.insert(id1,"end", "dir 1",text=" Check For 1", values=("1", "2"))
#
# id2 = tree.insert("", 1, "dir2", text="Dir 2")
# tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))
#
# ##alternatively:
# tree.insert("", 3, "dir3", text="Dir 3")
# tree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))

tree.pack()
single.pack()
root.mainloop()