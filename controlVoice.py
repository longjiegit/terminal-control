from ctypes import windll
WM_APPCOMMAND = 0x319
APPCOMMAND_VOLUME_UP = 0x0a
APPCOMMAND_VOLUME_DOWN = 0x09
APPCOMMAND_VOLUME_MUTE = 0x08
class ControlVoice():
    def addVoice(self):
        hwnd=windll.user32.GetForegroundWindow()
        windll.user32.PostMessageA(hwnd,WM_APPCOMMAND,0,APPCOMMAND_VOLUME_UP*0x10000)

    def minusVoice(self):
        hwnd = windll.user32.GetForegroundWindow()
        windll.user32.PostMessageA(hwnd, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_DOWN * 0x10000)

    def muteVoice(self):
        hwnd = windll.user32.GetForegroundWindow()
        windll.user32.PostMessageA(hwnd, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_MUTE * 0x10000)

