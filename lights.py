
import colorsys
from ez_graphics_09 import*
from ez_touchscreen_09 import*
from ez_arduino_09 import * 
import time
 
# Initialize the Arduino
arduino_init()
green = 3
red = 5
blue = 6
# Configure Pins for an SPI device
arduino_configure_pin(green, PIN_PWM)
arduino_configure_pin(red, PIN_PWM)
arduino_configure_pin(blue, PIN_PWM)
 
# Configure for a 25% duty cycle
arduino_set_pwm(PIN_3, 0.25)
 
# Loop forever
clear_screen('black')
height = get_screen_height()
width = get_screen_width()
step = int(height/15)
boxStart = (width/2)-(height/2)
globalH = 360

def setLights(r,g,b):
    print r,g,b
    arduino_set_pwm(red,r)
    arduino_set_pwm(green,g)
    arduino_set_pwm(blue,b)
def drawHBox():
    x = (width/2)+(height/2)+20
    for y in range(height):
        H = (float(height)-y)/float(height)
        r,g,b = colorsys.hsv_to_rgb(float(H),0.999,0.999)
        set_color(int(r*255),int(g*255),int(b*255))
        fill_rect(x,y,50,2)
def drawColorBox(H):
    for x in range(0,height,step):
        for y in range(0,height,step):
            s = x/float(height)
            b = y/float(height)
            r,g,b = colorsys.hsv_to_rgb(H,s,b)
            set_color(int(r*255),int(g*255),int(b*255))
            fill_rect(x+boxStart,height-y-step,step,step)
            
drawHBox()
drawColorBox(globalH)
globalS = 1.0
globalB = 1.0
while True:
    bg = capture_image(0, 0, 800, 480)
    set_drawing_image(bg)
    touch = touchscreen_finger_point()
    if touch != None:
        x = touch['x']
        y = touch['y']
        if (boxStart < x < boxStart+height):
            globalS = (x - boxStart)/float(height)
            globalB = (height-y)/float(height)
            r,g,b = colorsys.hsv_to_rgb(globalH,globalS,globalB)
            set_color(int(r*255),int(g*255),int(b*255))
            fill_rect(0,0,50,50)
            setLights(r,g,b)
        elif (boxStart + height + 20 < x < boxStart + height + 70):
            globalH = (height-y)/float(height)
            r,g,b = colorsys.hsv_to_rgb(globalH,globalS,globalB)
            set_color(int(r*255),int(g*255),int(b*255))
            fill_rect(0,0,50,50)
            setLights(r,g,b)
            drawColorBox(globalH)
    set_drawing_image(None)
    draw_image(bg, 0, 0)
    time.sleep(0.01)
    
    
    
    
    
    