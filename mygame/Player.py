from pico2d import * 
from gfw import *
from Ball import *
import copy


class Player(Sprite):
	def __init__(self, filename, x, y, ball):
		super().__init__(filename,  x, y)
		self.initx = copy.deepcopy(self.x)
		self.inity = copy.deepcopy(self.y)
		self.ball = ball
		self.dx = 0
		self.dy = 0

	def handle_event(e):
		pass

	def update(self):
		self.x = self.initx - (self.ball.x - self.ball.initxy[0])
		self.y = self.inity - (self.ball.y - self.ball.initxy[1])

	def draw(self):
		self.image.draw(self.x, self.y)
