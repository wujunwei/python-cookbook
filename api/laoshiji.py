import string
from tkinter import *
from urllib.request import urlopen
import re
import pyperclip
from bs4 import BeautifulSoup
from urllib.parse import *


def set_text(a_string):
    pyperclip.copy(a_string)

data = {}


def copy_url(event):
    res = urlopen(data[lb.get(lb.curselection())])
    bs = BeautifulSoup(res.read(), "lxml")
    magnet = bs.find("textarea").get_text()
    set_text(magnet.strip())


def search():
    data.clear()
    html = urlopen(quote("http://www.zhizhu.so/q?kw=" + var.get(), safe=string.printable))
    bs = BeautifulSoup(html.read(), "lxml")
    items = bs.find_all("a", {"title": re.compile("^.*[^\s]+.*$"), "target": "_blank"})
    for item in items:
        if 'title' in item.attrs:
            p = re.compile('<[^>]+>')
            lb.insert(END, p.sub("", item.attrs['title']))
            data[p.sub("", item.attrs['title'])] = "http://www.zhizhu.so/"+item.attrs['href']

root = Tk()
root.geometry("500x400")
root.resizable(False, False)
var = StringVar()
Entry(root, textvariable=var).pack(side=TOP)
Button(root, text="search", command=search).pack(side=TOP)
lb = Listbox(root, width=200, selectmode=EXTENDED)
lb.pack(side=BOTTOM)
lb.bind('<Double-Button-1>', copy_url)
root.mainloop()
