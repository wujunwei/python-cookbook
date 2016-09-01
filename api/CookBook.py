from tkinter import *
from urllib.request import urlopen
import json

import requests


class CookBook(object):
    root = None
    url = "http://www.tngou.net/api/cook/"
    classify = {'美容': 1, "减肥": 10, "保健养生": 15, "人群": 52}
    ImagePrefix = (r"http://tnfs.tngou.net/image", r"http://tnfs.tngou.net/img")

    def __init__(self):
        self.root = Tk()
        self.root.title("CookBook")
        self.root.resizable(True, True)
        self.center_window(800, 800)

    def run(self):
        self.root.mainloop()

    def center_window(self, width, height):
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(size)

    def get_detail_json(self, select_id):
        result = requests.get(self.url + "show", params={'id': select_id})
        return result.text

    def get_list_json(self, classify_id, page=1, rows=20):
        result = requests.get(self.url + "list", params={'id': classify_id, 'page': page, 'rows': rows})
        return result.text

    def get_json_by_name(self, name):
        result = requests.get(self.url + "name", params={'name': name})
        return result.text

    def get_img_url(self, img):
        request = urlopen(self.ImagePrefix[0] + img)
        if request.getcode() == 200:
            return self.ImagePrefix[0] + img
        else:
            return self.ImagePrefix[1] + img

if __name__ == '__main__':
    cb = CookBook()
    cb.get_img_url("/cook/150802/6d4d8bee058f471ff8c8d307d433223b.jpg")
    cb.run()
