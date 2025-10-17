'''from tkinter import *
ak=Tk()
ak.geometry("400x500")
la=Label(ak,text="Hi")
la.grid(row=1,column=0)
f=Frame(ak,width=45,height=50,background="pink")
f.grid(row=0,column=0)
ak.mainloop()'''

from tkinter import *
root=Tk()
root.geometry("400x400")
f=Frame(root,width=500,height=100,background="red")
la=Label(f,text="this is new message",background="red",foreground="white",font=("Times New Roman",20,"bold"))
la.place(x=0,y=0)
f.place(x=50,y=10)  
root.mainloop()

