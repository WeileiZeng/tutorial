import win32gui,win32con,win32ui,struct
def click(handle, pos):

    client_pos = win32gui.ScreenToClient(handle, pos)

    tmp = win32api.MAKELONG(client_pos[0], client_pos[1])

    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)

    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp) 

    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)



def get_curpos():

    return win32gui.GetCursorPos()



def get_win_handle(pos):

    return win32gui.WindowFromPoint(pos)



def get_color(pos):

    hdc_screen = win32gui.CreateDC("DISPLAY", "", None)

    hmem_dc = win32gui.CreateCompatibleDC(hdc_screen)

    h_bitmap = win32gui.CreateCompatibleBitmap(hdc_screen, 1, 1)

    h_old_bitmap = win32gui.SelectObject(hmem_dc, h_bitmap)

    win32gui.BitBlt(hmem_dc, 0, 0, 1, 1, hdc_screen, pos[0], pos[1], win32con.SRCCOPY)  

    win32gui.DeleteDC(hdc_screen) 

    win32gui.DeleteDC(hmem_dc) 

    x = win32ui.CreateBitmapFromHandle(h_bitmap) 

    bits = x.GetBitmapBits(True)   

    return struct.unpack('I', bits)[0]
print get_curpos()
print get_color((100,100))
print get_win_handle((100,100))
