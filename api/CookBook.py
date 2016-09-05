from tkinter import *
from tkinter import messagebox
from urllib.request import urlopen
import json

import io
import requests
from PIL import Image
from PIL import ImageTk
from bs4 import BeautifulSoup


class CookBook(object):
    root = None
    __url = "http://www.tngou.net/api/cook/"
    __classify = {'美容': 1, "减肥": 10, "保健养生": 15, "人群": 52}
    __ImagePrefix = (r"http://tnfs.tngou.net/image", r"http://tnfs.tngou.net/img")
    __dataList = {}
    __page = 1
    __image = None
    top_frame = None
    bottom_frame = None
    left_frame = None
    canvas = None

    def __init__(self):
        # 初始化root
        self.root = Tk()
        self.root.title("CookBook")
        self.root.resizable(True, True)
        self.center_window(800, 700)
        # 初始化变量
        self.text = StringVar()
        self.selection = IntVar()
        self.sel = IntVar()
        # 初始化frame
        self.init_frame()
        self.init_canvas()
        self.root.mainloop()

    def init_frame(self):
        self.init_top()
        self.init_left()
        self.init_bottom()

    def init_top(self):
        if self.top_frame is None:
            self.top_frame = Frame(self.root)
            self.top_frame.pack(side=TOP)
            i = 0
            for (key, value) in self.__classify.items():
                Radiobutton(self.top_frame, indicatoron=0, variable=self.selection, text=key, value=value, command=lambda: self.change_list(1)).grid(row=0, column=i, sticky=W)
                i += 1
        #

    def init_bottom(self):
        self.bottom_frame = Frame(self.root, bg="white")
        self.bottom_frame.pack(side=BOTTOM)
        Label(self.bottom_frame, wraplength=400, text='请选择', textvariable=self.text).pack(side=RIGHT)

    def init_canvas(self, sel_id=None):
        if self.canvas is None:
            self.canvas = Canvas(self.root, width=300, height=300)
        else:
            self.canvas.destroy()
            self.canvas = Canvas(self.root, width=300, height=300)
        if sel_id is not None:
            try:
                detail = self.get_detail_json(sel_id)
                bs = BeautifulSoup(detail['message'], "lxml")
                temp = bs.find_all('p')
                self.text.set("\n".join(t.string for t in temp))
                img = detail['img']
                img = self.get_img_url(img)
                image_bytes = urlopen(img).read()
                data_stream = io.BytesIO(image_bytes)
                pil_image = Image.open(data_stream)
                self.__image = ImageTk.PhotoImage(pil_image)
                self.canvas.create_image(100, 50, image=self.__image)
                # self.canvas.create_text(300, 450, text=text, fill='blue')
            except Exception as e:
                print(e)
        self.canvas.pack(side=RIGHT)

    def init_left(self):
        if self.left_frame is None:
            self.left_frame = Frame(self.root, bg="green", width=100, height=700)
            self.left_frame.pack(side=LEFT)
        else:
            self.left_frame.pack_forget()
            self.left_frame = Frame(self.root, bg="green", width=100, height=700)
            self.left_frame.pack(side=LEFT)
        i = 0
        for var in self.__dataList:
            Radiobutton(self.left_frame, indicatoron=0, variable=self.sel, bg="yellow", text=var['name'], value=var['id'],
                        command=lambda: self.init_canvas(self.sel.get()), width=20).grid(row=i, column=0, sticky=W)
            i += 1

        if i != 0:
            Button(self.left_frame, bg="yellow", text="上一页", command=self.previous).grid(row=i, column=0, sticky=W)
            Button(self.left_frame, bg="yellow", text="下一页", command=self.next).grid(row=i, column=1, sticky=E)

    def next(self):
        self.__page += 1
        self.__dataList = self.get_list_json(self.selection.get(), self.__page)
        self.init_left()

    def previous(self):
        self.__page -= 1
        if self.__page < 1:
            self.__page = 1
        self.__dataList = self.get_list_json(self.selection.get(), self.__page)
        self.init_left()

    def change_list(self, page=None):
        if page is not None:
            self.__page = 1
        self.__dataList = self.get_list_json(self.selection.get(), self.__page)
        self.init_left()

    def center_window(self, width, height):
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(size)

    def get_detail_json(self, select_id):
        try:
            result = requests.get(self.__url + "show", params={'id': select_id})
            obj = json.loads(result.text)
            return obj
        except Exception as e:
            messagebox.askokcancel('error', '网络错误请保持网络通畅')
            print(e)

    def get_list_json(self, classify_id, page=1, rows=20):
        result = requests.get(self.__url + "list", params={'id': classify_id, 'page': page, 'rows': rows})
        obj = json.loads(result.text)
        return obj['tngou']

    def get_json_by_name(self, name):
        result = requests.get(self.__url + "name", params={'name': name})
        return result.text

    def get_img_url(self, img):
        request = urlopen(self.__ImagePrefix[0] + img)
        if request.getcode() == 200:
            return self.__ImagePrefix[0] + img
        else:
            return self.__ImagePrefix[1] + img


if __name__ == '__main__':
    cb = CookBook()
