import ctypes
import struct
import log.commlog as commlog

waveOutGetVolume = (
    ctypes.windll.winmm.waveOutGetVolume)

waveOutSetVolume = (
    ctypes.windll.winmm.waveOutSetVolume)

# 最小/最大音量的常量设定
MINIMUM_VOLUME = 0  # fader control (MSDN Library)
MAXIMUM_VOLUME = 4294967295  # fader control (MSDN Library)
class OsVoice():
    def setVolume(self,volume):
        print(volume)
        try:
            if not (MINIMUM_VOLUME <= volume <= MAXIMUM_VOLUME):
                commlog.logger.error("Volume out of range")

                # 按公式处理音量数值
            volume = volume * MAXIMUM_VOLUME / 100;
            print(int(volume))
            hwnd = ctypes.windll.user32.GetForegroundWindow()
            print(waveOutGetVolume(0x00FF,0))
            # 设置音量

            ret = waveOutSetVolume(0, int(volume))
            print(ret)

            if ret != 0:
                print(ret)
        except Exception as e:
            print(e)