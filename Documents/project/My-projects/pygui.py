<<<<<<< HEAD
from tkinter import *
root=Tk()
from PIL import Image, ImageTk
root.geometry("733x434")
root.title('software')
nik=Label(text="Welcome to my Software",bg="red",fg="white",padx='22',pady='7',font="comicsansms 34 bold")
#photo=PhotoImage(file='C:\Users\nikhi\Pictures\img.jpg')
image=Image.open('img.jpg')
img=ImageTk.PhotoImage(image)
label=Label(image=img)
buttoon=Button(root,text='enter',width=24)
#add.pack()
nik.pack(side=BOTTOM,anchor="nw",fill=X)
buttoon.pack()
label.pack()


root.mainloop()


=======
from tkinter import *
root=Tk()
from PIL import Image, ImageTk
root.geometry("733x434")
root.title('software')
nik=Label(text="Welcome to my Software",bg="red",fg="white",padx='22',pady='7',font="comicsansms 34 bold")
#photo=PhotoImage(file='C:\Users\nikhi\Pictures\img.jpg')
image=Image.open('img.jpg')
img=ImageTk.PhotoImage(image)
label=Label(image=img)
buttoon=Button(root,text='enter',width=24)
#add.pack()
nik.pack(side=BOTTOM,anchor="nw",fill=X)
buttoon.pack()
label.pack()


root.mainloop()


>>>>>>> ffa54a7009b3986a920100cbf48d0af75002874e
