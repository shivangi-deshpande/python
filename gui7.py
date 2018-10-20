import tkinter as tk
import gui6 as tktable

def table_test():
    #### DEFINES THE INTERFACE ####
    master = tk.Tk()
    master.geometry('500x200+250+200')
    master.title('Dogs')
    #### DEFINING THE TABLE ####
    tb = tktable.Table(master,
                       state='disabled',
                       width=50,
                       titlerows=1,
                       rows=5,
                       cols=4,
                       colwidth=20)

    columns = ['Breed','Price','Location','Age']
    #### LIST OF LISTS DEFINING THE ROWS AND VALUES IN THOSE ROWS ####
    values = [['Doodle','1500','Chicago','1'],
              ['Pug','700','Kansas City','2'],
              ['Westie','1000','Lincoln','1'],
              ['Poodle','900','Atlanta','2']]
    #### SETS THE DOGS INTO THE TABLE ####
    #### VVVVVVVVVVVVVVVVVVVVVVVVVVV ####
    #DEFINING THE VAR TO USE AS DATA IN TABLE
    var = tktable.ArrayVar(master)
    row_count=0
    col_count=0
    #SETTING COLUMNS
    for col in columns:
        index = "%i,%i" % (row_count,col_count)
        var[index] = col
        col_count+=1
    row_count=1
    col_count=0
    #SETTING DATA IN ROWS
    for row in values:
        for item in row:
            print(item)
            index = "%i,%i" % (row_count,col_count)
            ## PLACING THE VALUE IN THE INDEX CELL POSITION ##
            var[index] = item
            #### IGNORE THIS IF YOU WANT, JUST SETTING SOME CELL COLOR ####
            try:
                if int(item) > 999:
                    tb.tag_cell('green',index)
            except:
                pass
            ###############################################################
            col_count+=1
        col_count=0
        row_count+=1
    #### ABOVE CODE SETS THE DOG INTO THE TABLE ####
    ################################################
    #### VARIABLE PARAMETER SET BELOW ON THE 'TB' USES THE DATA DEFINED ABOVE ####
    tb['variable'] = var
    tb.pack()
    #tb.tag_cell('green',index)
    tb.tag_configure('green', background='green')
    #### MAINLOOPING ####
    tk.mainloop()
table_test()