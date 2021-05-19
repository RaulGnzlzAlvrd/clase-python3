from Time2 import *
import time

class Cronometro:
	def __init__(self):
		self.reset()

	def play(self):
		self.start = now() 
	
	def stop(self):
		self.end = now()
	
	def reset(self):
		self.start = now()
		self.end = now()

	def __str__(self):
		duration = int_to_time(self.end - self.start)
		return str(duration)

def now():
	return time.time()

