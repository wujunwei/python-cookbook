# coding: utf-8
import os
import inspect

__name__ = "api"

class_arr = []

now_dir = inspect.stack()[0][1]
now_dir = os.path.dirname(now_dir)

files = os.listdir(now_dir)
if files is not None:
    for file in files:
        if os.path.splitext(file)[1] == ".py" and file != "__init__.py":
            class_arr.append(os.path.splitext(file)[0])


def run(class_name):
    if class_name in class_arr:
        module = __import__("api." + class_name, fromlist=class_name)
        getattr(module, class_name)()
        return True
    else:
        return False
