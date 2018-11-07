from time import sleep
from sense_hat import SenseHat
#get_accelerometer_raw  gives x,y,z axis data
#dont forget to change the values for the if statements
#use sens.clear()

sense = SenseHat()
green = (0,255,0)
yellow = (0,255,255)
red = (255,0,0)
ref = sense.get_accelerometer_raw()
x = ref['x']
y = ref['y']
z = ref['z']
while True:
	cur = sense.get_accelerometer_raw()
	a = cur['x']
	b = cur['y']
	c = cur['z']
	
	difa = abs(x-a)
	difb = abs(y-b)
	difc = abs(z-c)
	if difa > 5 or difb >5 or difc > 5:
		for i in range(50):
			sense.set_pixels(yellow)
			sleep(0.1)
			if difa >10 or difb > 10 or difc > 10:
				break
	if difa > 10 or difb > 10 or difc > 10:
		sense.set_pixels(red)
		sleep(10)
	if difa < 5 or difb < 5 or difc < 5:
		sense.set_pixels(green)
