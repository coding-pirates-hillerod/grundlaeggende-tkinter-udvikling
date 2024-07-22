from tkinter import Tk, PhotoImage, Label

root = Tk()

cookie_img = PhotoImage("./cookie.gif")

img_label = Label(root, image=cookie_img)
img_label.pack()

root.mainloop()
