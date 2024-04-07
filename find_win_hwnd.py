import win32gui
 
# GetDesktopWindow 获得代表整个屏幕的一个窗口（桌面窗口）句柄
hd = win32gui.GetDesktopWindow()
 
# 获取所有子窗口
hwndChildList = []
 
win32gui.EnumChildWindows(hd, lambda hwnd, param: param.append(hwnd), hwndChildList)
 
for hwnd in hwndChildList:

    if '斗地主' in win32gui.GetWindowText(hwnd):
        print("句柄：", hwnd, "标题：", win32gui.GetWindowText(hwnd))
        # f.write("句柄：" + str(hwnd) + " 标题：" + win32gui.GetWindowText(hwnd) + '\n')
        hwnd = win32gui.FindWindow(0,win32gui.GetWindowText(hwnd))#寻找窗口
        if not hwnd:
            print("找不到该窗口")
        else:
            win32gui.SetForegroundWindow(hwnd)#前置窗口