import tkinter.font as tkFont
import tkinter.ttk as ttk
from GetAllInformation import getProcessHeader, getProcessInfo
from tkinter import Tk, BOTTOM, BOTH, TOP, LEFT, RIGHT
import psutil


class Process(object):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self, container):
        self.container = container
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        s = """\
click on header to sort by that column
to change width of column drag boundary
        """
        # container = ttk.Frame(width=800, height=500)
        #
        # container.pack(fill='both', expand=True)

        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=process_header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
                            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
                            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
                            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=self.container)
        vsb.grid(column=1, row=0, sticky='ns', in_=self.container)
        hsb.grid(column=0, row=1, sticky='ew', in_=self.container)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in process_header:
            self.tree.heading(col, text=col.title(),
                              command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                             width=tkFont.Font().measure(col.title()))
        for item in process_info:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(process_header[ix], width=None) < col_w:
                    self.tree.column(process_header[ix], width=col_w)


def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
            for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    # data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
                                                     int(not descending)))




class Resource(object):
    def __init__(self, container):
        pass

class FileSystem(object):
    def __init__(self, container):
        pass




# the Process Information data ...
process_header = getProcessHeader()#['Process Name', 'User', '% CPU', 'ID', 'Status']

# getting Information about the Process
process_info = getProcessInfo()

# for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
#     list_info = list()
#
#     p = psutil.Process(int(proc.info['pid']))
#     list_info.append(proc.info['name'])
#     list_info.append(proc.info['username'])
#     list_info.append(p.cpu_percent())
#     list_info.append(proc.info['pid'])
#     list_info.append(p.status())
#     process_info.append(tuple(list_info))

root = Tk()
root.minsize(width=900, height=400)
root.config(bg='white')
root.wm_title("System Monitor")

top = ttk.Frame(root)
processFrame = ttk.Frame(root)
resouresFrame = ttk.Frame(root)
filesystemFrame = ttk.Frame(root)

top.pack(side=TOP)

Process(processFrame)
Resource(resouresFrame)
FileSystem(filesystemFrame)

def ProcessDisplay():
    processFrame.pack(side=BOTTOM, fill=BOTH, expand=True)
    resouresFrame.pack_forget()
    return


def ResourcesDisplay():
    processFrame.pack_forget()
    filesystemFrame.pack_forget()
    resouresFrame.pack(side=BOTTOM, fill=BOTH, expand=True)
    return


def FileSystemDisplay():
    processFrame.pack_forget()
    filesystemFrame.pack_forget()

    root.destroy()
    return


btn1 = ttk.Button(root, text="Process", command=ProcessDisplay)
btn2 = ttk.Button(root, text="Resources", command=ResourcesDisplay)
btn3 = ttk.Button(root, text="File System", command=FileSystemDisplay)
btn1.pack(in_=top, side=LEFT, pady=10)
btn2.pack(in_=top, side=LEFT, pady=10)
btn3.pack(in_=top, side=LEFT, pady=10)

root.mainloop()
