import random
import pokego
from time import sleep

while(True):
	pokego.crawler()
	sleep(200+random.randint(-20,20))

