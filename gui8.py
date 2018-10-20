import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk


class McListBox():
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self, container):
        self.tree = None
        self._setup_widgets()
        self._build_tree()
        self.container = container
        print('Here I Am')
    def _setup_widgets(self):
        s = """\
click on header to sort by that column
to change width of column drag boundary
        """

        # container = ttk.Frame(width=800, height=500)
        #
        # container.pack(fill='both', expand=True)
        # # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=car_header, show="headings")
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
        for col in car_header:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))
        for item in car_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(car_header[ix],width=None)<col_w:
                    self.tree.column(car_header[ix], width=col_w)
def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))
# the test data ...
car_header = ['Process Name', 'User', '% CPU', 'ID', 'Memory']
car_list = [
('Hyundai', 'brakes', '50%', '1', '9876') ,
('Honda', 'light', '50%', '1', '9876') ,
('Lexus', 'battery', '50%', '1', '9876') ,
('Benz', 'wiper', '50%', '1', '9876') ,
('Ford', 'tire', '50%', '1', '9876') ,
('Chevy', 'air', '50%', '1', '9876') ,
('Chrysler', 'piston', '50%', '1', '9876') ,
('Toyota', 'brake pedal', '50%', '1', '9876') ,
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876'),
('BMW', 'seat', '50%', '1', '9876')
]
# root = tk.Tk()
# root.minsize(width=900, height=400)
# root.wm_title("multicolumn ListBox")
# container = ttk.Frame(width=800, height=500)
#
# container.pack(fill='both', expand=True)
# mc_listbox = McListBox(container)
# root.mainloop()

