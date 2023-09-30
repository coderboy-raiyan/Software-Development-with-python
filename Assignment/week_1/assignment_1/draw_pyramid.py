import pyautogui

n = int(input())


def draw_pyramid():
    pyramid = ""
    for i in range(1, n+1):
        for j in range(1, i+1):
            pyramid += "#"
        pyramid += "\n"
    return pyramid


pyramid_str = draw_pyramid()
print(pyramid_str)
pyautogui.write(pyramid_str, interval=0.25)


pyautogui.hotkey('ctrl', 'z')
pyautogui.press("enter")
