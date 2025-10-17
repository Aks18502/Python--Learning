from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Tkinter Combobox Example")

l=Label(root,text="Choose an option")
l.pack(padx=10,pady=10)

options=[" ","option 1","option 2","option 3","option 4"]
combobox=ttk.Combobox(root,values=options)
combobox.pack(padx=10,pady=10)

combobox.set(options[0])

def show_selection():
    print("selected",combobox.get())

b=Button(root,text="Submit",command=show_selection)
b.pack(padx=10,pady=10)

root.mainloop()