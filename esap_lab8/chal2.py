from sense_hat import SenseHat
from time import sleep
from PIL import Image
import numpy as np
import scipy.io

def load_image(values,sense):
        for i in range(0,7):
                for j in range(0,7):
                        sense.set_pixel(i,j,values[i][j])


def clear_leds(sense):
	sense.clear()

path_to_file = "image"
im = Image.open(path_to_file)
rgb_im = im.convert('RGB')
valyes = np.array(rgb_im)

sense = SenseHat()

clear_leds(sense)

load_image(values,sense)

sense.flip_v()
sense.set_rotation(270)
