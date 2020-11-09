import display as dsp
import time
import numpy as np
import random

global display


def _parse_img(num):
	if num % 5 == 0:
		# use global display
		global display
		
		# random img
		img = np.ones((256,256,1), np.uint8)
		for row in range(img.shape[0]):
			for col in range(img.shape[1]):
				img[row,col,0] = random.randint(0, 255)
		
		# put img on display queue to show it
		display.show(img)
	else:
		pass


# function which processes every image before show it at display
# function take img1 argument and return img2
def img_processing(img1):
	# DO STH WITH IMG
	print('processing1')
	img2 = img1
	print('processing2')
	return img2


if __name__ == '__main__':
	
	global display	
	display = dsp.DisplayManager(name='Dispaly Example', # disply name
								interval=0.5, # sleep time [s]
								size=30, # queue size
								on_update=img_processing) # function called to process img before show it on screen
	
	# sth like main
	for i in range(100):
		print('for ', i)
		time.sleep(0.1)
		
		if i % 5 == 0:
			_parse_img(i)
	
	# finish thread
	display.finish()
	
	
	

