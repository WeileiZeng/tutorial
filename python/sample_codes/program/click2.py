import win32gui,win32api
DialogName=
win = win32gui.FindWindow(None,DialogName)
while win == 0:
    win = win32gui.FindWindow(None,DialogName)

time.sleep(X) 
hbtn = win32gui.FindWindowEx(win,None,None,ButtonName)
(left,top,right,bottom) = win32gui.GetWindowRect(hedit)

win32api.SetCursorPos((left+(right-left)/2,top+(bottom-top)/2)) 
time.sleep(0.5)


win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)
