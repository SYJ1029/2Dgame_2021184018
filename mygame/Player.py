from pico2d import * 
from gfw import *
from Ball import *
import copy
from math import *


class Player(Sprite):
	def __init__(self, filename, x, y, ball, num):
		super().__init__(filename,  x, y)
		self.initx = copy.deepcopy(self.x)
		self.inity = copy.deepcopy(self.y)
		self.ball = ball
		self.dx = 0
		self.dy = 0
		self.speed = 0.01
		self.num = num

	def handle_event(e):
		pass

	def move(self):
		# self.initx += (self.ball.x - self.initx) * self.speed
		# self.inity += (self.ball.y - self.inity) * self.speed
		pass

	def dist(self):
		x = self.ball.x - self.initx
		y = self.ball.y - self.inity

		return sqrt(x ** 2 + y ** 2)

	def update(self):
		if(self.ball.defnum == self.num):
			self.move()

		self.x = self.initx - (self.ball.dx * self.ball.t) * 4
		self.y = self.inity - (self.ball.dy * self.ball.t) * 4

		self.ball.distlist.append(self.dist())

	def draw(self):
		self.image.draw(self.x, self.y)
