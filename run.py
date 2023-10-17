print("init...")
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getchh = _Getch()

import os
import subprocess
import shutil

targetDir = "Desktop"
targetFormat = "mp3"
#todo
proxies = "proxies.txt"

def getch():
    return getchh().decode("utf-8") 
    #depc, it cant visualize ESC 

def Dumpproducttodesktop():
    # destination = os.path.join(os.path.join(os.environ['USERPROFILE']), targetDir)
    destination = os.path.normpath(os.path.expanduser("~/" + targetDir))
    source = os.getcwd() + "\product"
    # print(targetDir)

    allfiles = os.listdir(source)
    ress = 0
    for f in allfiles:
        ress = 1
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination, f)
        shutil.move(
            src_path,
            dst_path)
    
    return ress

def CarryOut(x):
    # x | <link> 
    # x = "nx_ref.exe " + x
    print("format:", targetFormat)
    x = "nx_ref.exe --path product --ffmpeg-location bin -x --audio-format " + str(targetFormat) + " " + x
    os.system(x)
    return 1

def getresponse():
    ino = b'w'
    ress = 0 # ESC
    while (ino != b'a' and ino != b'\x1b' and ino != b'e'):
        print("enter [ESC -ext]or [a - asset take] or [e - settings]")
        ino = getchh()
        print("bytecode",ino)
    
    if (ino == b'a'):
        ress = 1
    elif (ino == b'e'):
        ress = 2
    
    return ress

def geturl():
    ino = input("\n\n\n\n\n\n\nCTRL-V url ex.(https://www.youtube.com/watch?v=I9VfWCyCagQ)\n: ")
    
    return ino #"https://www.youtube.com/watch?v=baLFdrPt0SQ"

#https://www.youtube.com/watch?v=baLFdrPt0SQ

while (1):
    ress = getresponse()
    print("opcode", ress)
    if (ress == 0):
        #exit
        break
    elif (ress == 2):
        print(" open config.yml\npress any key to exit")
        darby = getch()
        break
    url = geturl()
    url = CarryOut(url)


    print("\n\n\n")
    
    try:
        url = Dumpproducttodesktop()
    except Exception as error:
        print("e- ", error)
        print("dumping error.! your "+ targetFormat+" will be stored in product")
    
    if (url == 1):
        # there was something htere, maybe it was a success?
        print("success - moved to USER" + targetDir)
    
    print("task finished - richard\n\n\n")
    # else continue