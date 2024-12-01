from pico2d import * 
from gfw import *
from Ball import *


class Player(Sprite):
	def __init__(self, filename, x, y):
		super().__init__(filename,  x, y)

	def handle_event(e):
		pass

	def update(self):
		pass

	def draw(self):
		self.image.draw(self.x, self.y)
