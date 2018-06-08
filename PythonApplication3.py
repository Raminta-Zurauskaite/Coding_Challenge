from tkinter import *
from tkinter import ttk

#root window
root = Tk()
root.title("To do list")

#functions
def add_task():
    pass


#variables
task_name = StringVar()

#mainframe
mainframe = ttk.Frame(root, padding="0 1 1 0")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
root.resizable(False, False)
n = ttk.Notebook(mainframe)
f1 = ttk.Frame(n)        
n.add(f1, text='List of tasks')


#text input
txt_input = ttk.Entry(f1,width=40, textvariable=task_name)
#button for text input
btn_add_task = ttk.Button(f1, text='Add task', command = add_task)
btn_add_task.grid(column=1, columnspan=2, row= 1)

root.mainloop()