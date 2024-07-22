from tkinter import Tk, PhotoImage, Label

root = Tk()

image = PhotoImage(file="./cookie.jpg")

img_label = Label(root, image=image)
img_label.pack()

root.mainloop()
