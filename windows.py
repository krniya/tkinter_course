from ctypes import windll


def set_dpi_awareness():
    try:
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass