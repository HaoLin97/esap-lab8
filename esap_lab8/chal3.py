from sense_hat import SenseHat
import numpy as np
from time import sleep

def add_dangerous_pixels(sense,nr_dang_pix):
	dangerous_coord = []
	for i in range(0,nr_dang_pix):
		x = np.random.randint(0,8)
		y = np.random.randint(0,8)
		candidate_pixel = (x,y)
		dangerous_coord.append(candidate_pixel)
return dangerous_coord

def check_boundary(x,y):

return x,y

sense = SenseHat()
sense.clear()

number_of_dangerous_pixels = 4
dangerous_coord = add_dangerous_pixels(sense,number_of_dangerous_pixels)

for set in dangerous_coord:
	print(set)
	##may have to initialise r
	sense.set_pixel(set[0],set[1],r)

white = (255,255,255)

x,y = 6,6
sense.set_pixel(x,y,white)

goal_pixel = (2,2)

##

sense.set_pixel(goal_pixel[0],goal_pixel[1],0,255,0)

alive = True
while alive:
	for event in sense.stick.get_events():
		if event.direction == 'up':
			sense.set_pixel(x,y,0,0,0)
			y -= 1
			x,y = check_boundary(x,y)
			sense.set_pixel(x,y,white)
		if event.direction == 'down':
			sense.set_pixel(x,y,0,0,0)
			y += 1
			x,y = check_boundary(x,y)
			sense.set_pixel(x,y,white)
		if event.direction == 'left':
			sense.set_pixel(x,y,0,0,0)
			x -= 1
			x,y = check_boundary(x,y)
			sense.set_pixel(x,y,white)
		if event.direction == 'right':
			sense.set_pixel(x,y,0,0,0)
			x += 1
			x,y = check_boundary(x,y)
			sense.set_pixel(x,y,white)
		if (x,y) in dangerous_coord:
			sense.show_message('Game over')
			print('Game Over)
			alive = False
		if (x,y) == (goal_pixel[0],goal_pixel[1]):
			sense.show_message('Victory')
			alive = False
