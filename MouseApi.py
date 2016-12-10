from ctypes import windll

def go_back():
    windll.user32.mouse_event(0x0180, 0, 0, 0x1, 0)

def go_forward():
    windll.user32.mouse_event(0x0180, 0, 0, 0x2, 0)

def scroll_up(pixel):
    windll.user32.mouse_event(0x0800, 0, 0, pixel, 0)

def scroll_down(pixel):
    windll.user32.mouse_event(0x0800, 0, 0, -pixel, 0)
