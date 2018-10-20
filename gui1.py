import time
import tkinter as tk
from tkinter import messagebox
mw = tk.Tk()

def change():
    white.pack_forget()
    back.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
    back.pack(fill=tk.BOTH, expand=1)  # Expand the frame to fill the root window

back = tk.Frame(master=mw,bg='black')
white = tk.Frame(master=mw, bg='white')#tk.Frame(master=mw, bg='white')

btn1 = tk.Button(master=white, text='First', command=change)
btn1.pack()
btn2 = tk.Button(master=white, text='Quit', command=mw.destroy)
btn2.pack()
lbl = tk.Label(master=white, text='First Label')
lbl.pack()

by = ""
def startgame():

    #by["text"] = "Good By"
    messagebox.showinfo("Hello Python", "Hello World")
    back.pack_forget()
    # white = tk.Frame(master=mw, bg='white')
    white.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
    white.pack(fill=tk.BOTH, expand=1)  # Expand

   # time.sleep(5)
    # mw.destroy()

    #
    back.pack()



mw.title('The game')

mw.geometry("800x500") #You want the size of the app to be 500x500
mw.resizable(0, 0) #Don't allow resizing in the x or y direction


back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window

#Changed variables so you don't have these set to None from .pack()
go = tk.Button(master=back, text='Start Game', command=startgame)
go.pack()
close = tk.Button(master=back, text='Quit', command=mw.destroy)
close.pack()
# for i in range(10):
#     info = tk.Label(master=back, text='Made by me!', bg='red', fg='black')
#     info.pack()
by = tk.Label(master=back, text="Change Frame")
by.pack()
mw.mainloop()