from tkinter import *
a=Tk()
b=Label(a, text="Name")
b.pack()
c=Entry(a)
c.pack()
def save():
    x=c.get() 
    print(x)
d=Button(a, text="Save", command=save)
d.pack()
a.mainloop()


'''from tkinter import *
root=Tk()
l1=Label(root,text="Name")
l1.pack()
e1=Entry(root)
e1.pack()
l2=Label(root,text="degree")
l2.pack()
e2=Entry(root)
e2.pack()

root.mainloop()'''