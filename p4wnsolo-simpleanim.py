#!/usr/bin/python
# -*- coding:utf-8 -*-

import SH1106
import time
import config
import traceback
import subprocess
import socket
import fcntl
import struct
import pathlib
from pathlib import Path
#import fontawesome as fa

from PIL import Image,ImageDraw,ImageFont

# Init variables
prefix = str(pathlib.Path(__file__).parent.resolve()) + '/'

prefix = prefix + 'fonts/'

fontfile1 = 'SFDistantGalaxyAlternate-It.ttf'
fontfile2 = 'SFDistantGalaxyOutline-Ital.ttf'
fontfile3 = 'SFDistantGalaxySymbols-Ital.ttf'


# Set font.  Default myfont = './fonts/DroidSansMono.ttf'
myfont = prefix + fontfile1  # Editor's number 1 pick
myfont2 = prefix + fontfile2  # Editor's number 1 pick
myfont3 = prefix + fontfile3  # Editor's number 1 pick
iconfont = prefix + 'fontawesome-webfont.ttf'  # FontAwesome   #fontawesome-webfont.ttf

iconsize = 25
theiconfont = ImageFont.truetype(iconfont, iconsize)    

#myfont = './fonts/DejaVuSansMono.ttf' ## Editor's number 2 pick
#myfont = './fonts/UbuntuMono-R.ttf'  ### Condensed!  Also try UbuntuMono-RI.ttf for Italic
#myfont = './fonts/disco.ttf    <---FUN!
#myfont = './fonts/HyperFont.ttf    <---FUN!
#myfont = './fonts/fantasquesansmono-regular.otf'    <---OTF! Just here for demo
#myfont = './fonts/SourceCodePro-XXXXX.ttf where XXXXX = Light, ExtraLight, Regular, Italic   # Good but the @ symbol looks weird
#FreePixel.ttf  ### Resembles old video games
#ProggyTiny.ttf  ### Readable even with ultra small font size
#nasa.otf  ### Futuristic, non-pixelated

#1:  Prototype
#2:  robot   ## Good "hacker" font
#3:  nasa

# check Prototype vs Robot in large and small text

#SFDistantGalaxy-Italic.ttf
#SFDistantGalaxyAltOutline-I.ttf
#SFDistantGalaxyAltOutline.ttf
#SFDistantGalaxyAlternate-It.ttf
#SFDistantGalaxyAlternate.ttf
#SFDistantGalaxyOutline-Ital.ttf
#SFDistantGalaxyOutline.ttf
#SFDistantGalaxySymbols-Ital.ttf
#SFDistantGalaxySymbols.ttf


fontsize1 = 35
fontsize2 = 37
fontsize3 = 14

# Get IP Address
def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address

try:
    disp = SH1106.SH1106()
    disp.Init()
    disp.clear()
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    font1 = ImageFont.truetype(myfont, fontsize1)
    font2 = ImageFont.truetype(myfont2, fontsize2)
    font3 = ImageFont.truetype(myfont3, fontsize3)
    draw.line([(0,0),(127,0)], fill = 0)
    draw.line([(0,0),(0,63)], fill = 0)
    draw.line([(0,63),(127,63)], fill = 0)
    draw.line([(127,0),(127,63)], fill = 0)

#    draw.text((0,1), ' ' + fontfile1, font = font1, fill = 0)
#    draw.text((0,fontsize1 + 1), ' ' + fontfile2, font = font2, fill = 0)
#    draw.text((0,fontsize1 + fontsize2), ' ' + fontfile3, font = font3, fill = 0)

    #draw.text((-7,4), ' P4WN', font = font1, fill = 0)
    #draw.text((-4,fontsize1), ' SOLO', font = font2, fill = 0)


    # Draw the text!
    #draw.text((0,20), faicon4, font = theiconfont, fill = 0)
    #draw.text((0,fontsize1 + fontsize2 + 15), '         Loading..', font = font3, fill = 0)

    i = 1
    j = 1
    k = 1
    thefill = 0

    while k < 26:
        if i == 1:
            faicon4 = 'o'
        elif i == 2:
            faicon4 = 'oo'
        elif i == 3:
            faicon4 = 'ooo'
        elif i == 4:
            faicon4 = 'oooo'
        elif i == 5:
            faicon4 = 'ooooo'
        elif i == 6:
            faicon4 = 'o'
            thefill = 1
        elif i == 7:
            faicon4 = 'oo'
            thefill = 1
        elif i == 8:
            faicon4 = 'ooo'
            thefill = 1
        elif i == 9:
            faicon4 = 'oooo'
            thefill = 1
        elif i == 10:
            faicon4 = 'ooooo'
            thefill = 1

        #image1=image1.rotate(i*(1)) #rotate image 
        draw.text((0,20), faicon4, font = theiconfont, fill = thefill)
        disp.ShowImage(disp.getbuffer(image1))
        time.sleep(0.05)
        print('i = ' + str(i))
        print('j = ' + str(j))
        print(faicon4)
        print('thefill = ' + str(thefill))
        if j == 4:
            k = 1
            if thefill == 0:
                thefill = 255
            elif thefill == 255:
                thefill = 0
        i = i + 1
        k = k + 1
        #j = j + 1
        #if i == 6:
        #    thefill = 255
            

    while i > 13:
        i = i - 1
        #image1=image1.rotate(i*(-1)) #rotate image 
        disp.ShowImage(disp.getbuffer(image1))
        time.sleep(0.2)

    exit()
#    image1=image1.rotate(-12) #rotate image 
#    disp.ShowImage(disp.getbuffer(image1))
#    time.sleep(15)    
#    Himage2 = Image.new('1', (disp.width, disp.height), 255)
#    bmp = Image.open('pic.bmp')
#    Himage2.paste(bmp, (0,0))    
#    disp.ShowImage(disp.getbuffer(Himage2))
#    time.sleep(2)
#    disp.clear()

#    image2 = Image.new('1', (disp.width, disp.height), "WHITE")
#    draw2 = ImageDraw.Draw(image2)
#    IPAddress = str(get_ip_address())
#    draw2.text((0,0), IPAddress, font = font1, fill = 0)
#    disp.ShowImage(disp.getbuffer(image2))

except IOError as e:
    print(e)
    
except KeyboardInterrupt:    
    print("ctrl + c:")
    epdconfig.module_exit()
    exit()
