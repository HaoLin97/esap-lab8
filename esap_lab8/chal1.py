from sense_hat import SenseHat
from time import sleep

def clear_leds(sense):
##
	sense.clear()
##



sense = SenseHat()
clear_leds(sense)

x = [255,0,0]
o = [255,255,255]

shape = [
x,x,x,x,o,o,o,o,
o,o,o,x,o,o,x,o,
o,o,o,x,o,o,x,o,
x,x,x,x,x,x,x,o,
x,o,o,x,o,o,o,o,
x,o,o,x,o,o,o,o,
o,o,o,x,x,x,o,o,
o,o,o,o,o,o,o,o,

]

sense.set_pixels(shape)

##
##
##

#sense.flip_v()
angle = 0
while True:
	if angle>270:
		angle = 0
	sense.set_rotation(angle)
	sleep(1)
	angle+=90
