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
import fontawesome as fa
import pathlib
from pathlib import Path

from PIL import Image,ImageDraw,ImageFont

# Init variables
prefix = str(pathlib.Path(__file__).parent.resolve()) + '/'

prefix = prefix + 'fonts/'

fontfile1 = 'SFDistantGalaxyAlternate-It.ttf'
fontfile2 = 'SFDistantGalaxySymbols-Ital.ttf'
fontfile3 = 'SFDistantGalaxyAltOutline.ttf'

# Set font.  Default myfont = './fonts/DroidSansMono.ttf'
myfont = prefix + fontfile1  # Editor's number 1 pick
myfont2 = prefix + fontfile2  # Editor's number 1 pick
myfont3 = prefix + fontfile3  # Editor's number 1 pick
iconfont = prefix + 'fontawesome-webfont.ttf'  # FontAwesome   #fontawesome-webfont.ttf

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


fontsize1 = 19
fontsize2 = 12
fontsize3 = 14

iconsize = 26
theiconfont = ImageFont.truetype(iconfont, iconsize)    

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

    draw.text((0,4), ' P4WNSOLO', font = font1, fill = 0)
    draw.text((0,fontsize1 + 4), '         htb|xj', font = font2, fill = 0)
    #draw.text((0,fontsize1 + fontsize2 + 15), '         Loading..', font = font3, fill = 0)

    # Set font-awesome icon
    faicon4 = fa.icons['chess-pawn'] + fa.icons['power-off'] + fa.icons['bluetooth'] + fa.icons['toggle-on'] + fa.icons['toggle-off'] + fa.icons['plug'] 
    #faicon4 = 'noOpP'

    # Draw the text!
    draw.text((0,fontsize1 + fontsize2 + 5), faicon4, font = theiconfont, fill = 0)


    #image1=image1.rotate(0) 
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(15)
    Himage2 = Image.new('1', (disp.width, disp.height), 255)
    bmp = Image.open('pic.bmp')
    Himage2.paste(bmp, (0,0))    
    disp.ShowImage(disp.getbuffer(Himage2))
    time.sleep(2)
    disp.clear()
    image2 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw2 = ImageDraw.Draw(image2)
    IPAddress = str(get_ip_address())
    draw2.text((0,0), IPAddress, font = font1, fill = 0)
    disp.ShowImage(disp.getbuffer(image2))

except IOError as e:
    print(e)
    
except KeyboardInterrupt:    
    print("ctrl + c:")
    epdconfig.module_exit()
    exit()
