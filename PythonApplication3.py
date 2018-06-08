from tkinter import *
from tkinter import ttk

#root window
root = Tk()
root.title("To do list")
root.geometry("200x300")

#list
tasks=[]

#for testing
tasks = ["Go to the store", "Clean the house"]

#functions
def update_listbox():
    for task in tasks:
        listbox.insert("end", task)

def add_task():
    update_listbox()


#variables
task_name = StringVar()

#mainframe
mainframe = ttk.Frame(root, padding="0 1 1 0")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
root.resizable(False, False)
n = ttk.Notebook(mainframe)       


#text input
txt_input = ttk.Entry(root,width=40, textvariable=task_name)
#button for text input
btn_add_task = ttk.Button(root, text='Add task', command = add_task)
btn_add_task.grid(row = 0, column = 0, columnspan=2, sticky=N)

listbox = Listbox(root, width=40)
listbox.grid(row = 1, column = 0, sticky=S)

root.mainloop()