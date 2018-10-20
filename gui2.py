from tkinter import Tk, RIGHT, BOTH, RAISED, TOP, LEFT, NE
from tkinter.ttk import Frame, Button, Style

import top as top


class Example(Frame):

    window = ""
    def __init__(self, window):
        super().__init__()
        self.window = window

        self.initUI()

    def initUI(self):
        self.master.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Close", command=self.window.destroy)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)


def main():
    root = Tk()
    root.geometry("700x500")

    btn1 = Button(master=root, text='Process')
    btn1.pack(padx=5, pady=5)
    btn2 = Button(master=root, text='CPU')
    btn2.pack()
    btn3 = Button(master=root, text='File System')
    btn3.pack()

    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()