from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('image')
root.geometry('400x400')

upload=Image.open("img.jpg")

image=imageTk.PhotoImage(upload)

label=(root, image=image, height=350, width=300)
label.place(x=40, y=0)
label2=Label(root, text="This is how you add image in Tkinter")

root.mainloop