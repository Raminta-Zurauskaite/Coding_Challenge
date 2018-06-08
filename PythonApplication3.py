from tkinter import *
from tkinter import ttk

root = Tk()
root.title("To do list")

mainframe = ttk.Frame(root, padding="0 1 1 0")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
root.resizable(False, False)
n = ttk.Notebook(mainframe)
f1 = ttk.Frame(n)        
n.add(f1, text='List of tasks')

task_name = StringVar()

txt_input = ttk.Entry(f1,width=40, textvariable=task_name)

btn_add_task = ttk.Button(f1, text='Add task', command = add_task)

root.mainloop()