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
		self.speed = 0.01

	def handle_event(e):
		pass

	def move(self):
		self.initx += (self.ball.x - self.initx) * self.speed
		self.inity += (self.ball.y - self.inity) * self.speed
		print(f'{self.ball.x - self.init.x}\n')

	def update(self):
		self.move()


		self.x = self.initx - (self.ball.dx * self.ball.t) * 4
		self.y = self.inity - (self.ball.dy * self.ball.t) * 4

	def draw(self):
		self.image.draw(self.x, self.y)
