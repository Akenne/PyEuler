from PIL.ImageGrab import grab
import os
import time
 
def screenGrab():
    box = ()
    im = grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()