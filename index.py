# -*- coding:utf-8 -*-
from tkinter import *
from tkinter import messagebox
import api


def find_class(event):
    class_name = lb.get(lb.curselection())
    if api.run(class_name) is False:
        messagebox.askokcancel('敬请期待', '功能还在开发中，敬请期待')


app = Tk()
app.title("工具箱")
app.geometry("200x300")
app.wm_attributes('-topmost', 1)
lb = Listbox(app)
with open("data/category") as file:
    lines = file.readlines()
    for line in lines:
        lb.insert(END, line.strip())
lb.bind("<Double-Button-1>", find_class)
lb.pack()
app.mainloop()
