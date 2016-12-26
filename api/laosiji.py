# -*- coding: utf-8 -*-
from tkinter import *
from urllib import parse
from urllib import request
import re
import pyperclip
from bs4 import BeautifulSoup


def set_text(a_string):
    pyperclip.copy(a_string)

data = {}


def copy_url(event):
    res = request.urlopen(data[lb.get(lb.curselection())])
    bs = BeautifulSoup(res.read(), "lxml")
    magnet = bs.find("textarea").get_text()
    set_text(magnet.strip())


def search():
    data.clear()
    lb.delete(0, len(data))
    url = "http://www.zhizhu88.com/q?kw=" + parse.quote(var.get(), safe=':/?=')
    html = request.urlopen(url)
    bs = BeautifulSoup(html.read(), "lxml")
    items = bs.find_all("a", {"href": re.compile("^bt/\w+.html$")})
    for item in items:
        if 'href' in item.attrs:
            p = re.compile('<[^>]+>')
            lb.insert(END, p.sub("", item.attrs['title']))
            data[p.sub("", item.attrs['title'])] = "http://www.zhizhu.so/"+item.attrs['href']

root = Tk()
root.geometry("500x400")
root.title("搜索")
root.resizable(False, False)
var = StringVar()
Entry(root, textvariable=var).pack(side=TOP)
Button(root, text="search", command=search).pack(side=TOP)
lb = Listbox(root, width=200, selectmode=EXTENDED)
lb.pack(side=BOTTOM)
lb.bind('<Double-Button-1>', copy_url)
root.mainloop()
