from tkinter import *
import api


def find_class():
    print(lb.get(lb.curselection()))


def load_class(event):
    print("werw")

top = Tk()
lb = Listbox(top)
with open("data/category") as file:
    data = file.readline()
    lb.insert(END, data)
lb.bind("click", load_class)
lb.pack()
top.mainloop()
