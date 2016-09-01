from tkinter import *


class CookBook(object):
    root = None

    def __init__(self):
        self.root = Tk()
        self.root.resizable(True, True)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    cb = CookBook()
    cb.run()
