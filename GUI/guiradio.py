from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root=Tk()
root.title("MALL")

f1=Frame(root,width=1500,height=100,background="green")
f1.place(x=0,y=0)
l1=Label(f1,text="AKS MALL",background="green",foreground="purple",font=("Blackadder ITC",28,"bold"))
l1.place(x=520,y=25)

f2=Frame(root,width=1000,height=100,background="orange")
f2.place(x=0,y=610)
l2=Label(f2,text="Created by AKS in 2025",background="orange",foreground="green",font=("blackadder ITC",28,"bold"))
l2.place(x=520,y=25)

bg_image=Image.open("mall.jpg")
bg_photo=ImageTk.PhotoImage(bg_image.resize((200,100)))

bg_label=Label(root,image=bg_photo)
bg_label.place(x=0,y=100,relwidth=1,relheight=1)


root.mainloop()