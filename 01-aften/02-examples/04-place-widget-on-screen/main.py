# Step 1 - import og initialiser TKinter
from tkinter import Tk, Label

root = Tk()

# Step 2 - initialiser en "Widget"
my_label = Label(root, "Hello, World!")

# Step 3 - placer "Widget" på skærmen
my_label.pack()
