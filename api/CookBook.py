from tkinter import *


class CookBook(object):
    root = None

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


if __name__ == '__main__':
    cb = CookBook()
    cb.run()
