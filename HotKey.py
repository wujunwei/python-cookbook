import ctypes
import threading

import win32con


class HotKey(threading.Thread):  # 创建一个Thread.threading的扩展类
    def __init__(self, group=None, name=None,
                 args=(), kwargs=None, *, daemon=True):
        super().__init__(group=group, target=self.run, name=name,
                         args=args, kwargs=kwargs, daemon=daemon)

    def run(self):
        user32 = ctypes.windll.user32  # 加载user32.dll
        if not user32.RegisterHotKey(None, 99, win32con.MOD_ALT, 65):  # 注册快捷键 alt + a 并判断是否成功。
            exit()
        if not user32.RegisterHotKey(None, 100, win32con.MOD_ALT, 66):  # 注册快捷键 alt + b 并判断是否成功。
            exit()
        # 以下为判断快捷键冲突，释放快捷键
        try:
            msg = ctypes.wintypes.MSG()
            # print msg
            while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    if msg.wParam == 99:
                        root.withdraw()
                    if msg.wParam == 100:
                        root.update()
                        root.deiconify()
                user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, 1)