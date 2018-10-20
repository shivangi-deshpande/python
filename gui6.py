from doctest import master

from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel
from tkinter import *


tframe = Frame(master)
tframe.pack()
table = TableCanvas(tframe)
table.createTableFrame()


model = TableModel()
table = TableCanvas(tframe, model=model)

table.redrawTable()

data = dict()

model = table.model
model.importDict(data) #can import from a dictionary to populate model
table.redrawTable()