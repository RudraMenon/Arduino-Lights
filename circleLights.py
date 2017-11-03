from ez_graphics_09 import*
from ez_touchscreen_09 import*
import math,time

clear_screen('white')
set_color('black')

def getDistance(x,y):
    return ((y-240.0)**2+(x-400.0)**2)**0.5

def getAngle(x,y):
    rad = math.atan2(y-240,x-400)
    return math.degrees(rad) 
   
def getColor(deg):
    if deg < 0:
        deg += 360
    red,green,blue = 0,0,0
    if (0 <= deg <= 60):
        red = 255
        green = 255-((deg)*255.0/120.0)
    elif(60 < deg <= 120):
        red = 255
        blue = ((deg-60)*255.0/120.0)
    elif(120 < deg <= 180):
        blue = 255
        red = 255-((deg-120)*255.0/120.0)
    elif(180 < deg <= 240):
        blue = 255
        green = (deg-180)*255.0/120.0
    elif(240 < deg <= 300):
        green = 255
        blue = 255 - ((deg-240)*255.0/120.0)
    elif(300 < deg <= 360):
        green = 255
        red = (deg-240)*255.0/120.0
    return (int(red),int(green),int(blue))
    
def colorCircle():
    for y in range(0,480):
        for x in range(160,640):
            if getDistance(x,y) < 240:
                r,g,b = getColor(getAngle(x,y))
                set_color(r,g,b)
                fill_rect(x,y,1,1)
                
draw_circle(400,240,240)
colorCircle()
while 1:
    time.sleep(1)