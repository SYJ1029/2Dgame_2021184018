from pico2d import * 
from gfw import *
from Ball import *
import copy
from math import *


def dist(x, y):

	return sqrt(x ** 2 + y ** 2)

class Player(Sprite):
	def __init__(self, filename, x, y, ball, base, num):
		super().__init__(filename,  x, y)
		self.initx = copy.deepcopy(self.x)
		self.inity = copy.deepcopy(self.y)
		self.ball = ball
		self.base = base
		self.baseIndex = 0

		self.dx = 0
		self.dy = 0
		self.speed = 0.005
		self.num = num
		self.catch = False


	def handle_event(self, e):
		if e.type == SDL_KEYDOWN and e.key == SDLK_a:
			self.ball.godraw = True
			self.baseIndex = 2
			

	def move(self):
		if(self.ball.defnum == self.num):
			self.initx += (self.ball.x - self.initx) * self.speed
			self.inity += (self.ball.y - self.inity) * self.speed
		
			overlap = self.GetOverlapBox()

			if overlap != None:
				self.ball.godraw = False
				self.catch = True
		else:
			if(self.num <= 7 and self.num > 1):
				self.initx += (self.base[self.baseIndex].x - self.initx) * self.speed
				self.inity += (self.base[self.baseIndex].y - self.inity) * self.speed


	def dist(self):
		x = (self.ball.initpos[0] + self.ball.dx) - self.initx
		y = (self.ball.initpos[1] + self.ball.dy) - self.inity

		return sqrt(x ** 2 + y ** 2)

	def update(self):

		self.move()

		self.x = self.initx - (self.ball.dx * self.ball.t)
		self.y = self.inity - (self.ball.dy * self.ball.t)


		self.ball.distlist.append([self.dist(), self.num])



	def draw(self):
		self.image.draw(self.x, self.y)


	def GetOverlapBox(self):
		playerbb = [[self.initx - 20, self.inity - 20], 
			[self.initx + 20, self.inity + 20]]

		ballbb = [[self.ball.x - self.ball.ballwidth / 2, self.ball.y - self.ball.ballwidth / 2], 
    		[self.ball.x + self.ball.ballwidth / 2, self.ball.y + self.ball.ballwidth / 2]]

		overlap1 = [max(playerbb[0][0], ballbb[0][0]), max(playerbb[0][1],ballbb[0][1])]
		overlap2 = [min(playerbb[1][0], ballbb[1][0]), min(playerbb[1][1], ballbb[1][1])]
		# print(f'overlapbb: {list(overlap1)}, {list(overlap2)}')

		if overlap1[0] < overlap2[0] and overlap1[1] < overlap2[1]:
			return [overlap1, overlap2]
		else:
			return None  # 겹치는 영역 없음
		






