import tkinter as tk
from tkinter import ttk

class Window():
    def __init__(self, parent):
        self.parent = parent
        self.parent.minsize(width=900, height=400)
        self.widgets()

    def widgets(self):
        s1 = ttk.Style()
        s1.theme_use('classic')
        s1.configure('TNotebook.Tab', background='navajo white')
        s1.map('TNotebook.Tab', background=[('selected', 'goldenrod'), ('active', 'goldenrod')])

        self.nb1 = ttk.Notebook(self.parent)
        self.nb1.place(relx=0.1, rely=0.1, width=500, height=200)
        self.tab1 = ttk.Frame(self.nb1)
        self.tab2 = ttk.Frame(self.nb1)
        self.tab3 = ttk.Frame(self.nb1)
        self.nb1.add(self.tab1, text='Tab1')
        self.nb1.add(self.tab2, text='Tab2')
        self.nb1.add(self.tab3, text='Tab3')
        self.b1 = ttk.Button(self.parent, text='Quit', command=self.quit)
        self.b1.place(relx=0.4, rely=0.7, height=70, width=150)

    def quit(self):
        self.parent.destroy()

root = tk.Tk()
app = Window(root)
root.mainloop()