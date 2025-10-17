from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root=Tk()
root.title("Image")
root.geometry("400x400")

bg_image=Image.open("mall.jpg")
bg_photo=ImageTk.PhotoImage(bg_image.resize((500,400)))

bg_label=Label(root,image=bg_photo)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

b=Button(bg_label,text="Submit")
b.pack(padx=50,pady=50)
root.mainloop()