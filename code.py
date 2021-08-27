
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

pixel_pin = board.D1
num_pixels = 12

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1
, auto_write=False)



YELLOW = (255,222,0)

def turnsignal_right():
	pixels.fill((0,0,0))
	pixels.write()
	time.sleep(0.15)
	pixels[0] = YELLOW
	pixels[11] = YELLOW
	pixels.write()
	time.sleep(0.15)
	pixels[4] = YELLOW
	pixels[7] = YELLOW
	pixels.write()
	time.sleep(0.15)
	pixels[3] = YELLOW
	pixels[8] = YELLOW
	pixels.write()
	time.sleep(0.15)

def turnsignal_left():
	pixels.fill((0,0,0))
	pixels.write()
	time.sleep(0.15)
	pixels[2] = YELLOW
	pixels[9] = YELLOW
	pixels.write()
	time.sleep(0.15)
	pixels[4] = YELLOW
	pixels[7] = YELLOW
	pixels.write()
	time.sleep(0.15)
	pixels[5] = YELLOW
	pixels[6] = YELLOW
	pixels.write()
	time.sleep(0.15)
	

while True:
	if switch.value:
		turnsignal_right()
	else:
		turnsignal_left()
	