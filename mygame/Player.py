from pico2d import * 
from gfw import *
from Ball import *
import copy
from math import *
from ScoreMenual import *
from SBOBox import *
def dist(x, y):

	return sqrt(x ** 2 + y ** 2)

class Player(Sprite):
	def __init__(self, filename, x, y, ball, num):
		super().__init__(filename,  x, y)
		self.initx = copy.deepcopy(self.x)
		self.inity = copy.deepcopy(self.y)
		self.x = copy.deepcopy(self.initx)
		self.y = copy.deepcopy(self.inity)
		self.ball = ball
		self.baseIndex = 5
		self.t = 0

		self.dx = 0
		self.dy = 0
		self.speed = 0.005
		self.num = num
		self.catch = False
		self.Bat = True
		self.token = [copy.deepcopy(self.initx), copy.deepcopy(self.inity)]

	def InitBase(self, base):
		self.base = base

	def handle_event(self, e):
		if e.type == SDL_KEYDOWN:
			if self.catch == True and self.baseIndex < 4:
				if e.key == SDLK_a or e.key == SDLK_w or e.key == SDLK_s or e.key == SDLK_d:
					self.ball.godraw = True
					self.catch = False
			

	def move(self):
		global Score, ScoreIndex, Strike, Ballcount, Out, attackSequence
		if(self.Bat == True and self.ball.defnum == self.num):
			
			# self.initx += (self.ball.x - self.token[0]) * self.speed
			# self.inity += (self.ball.y - self.token[1]) * self.speed
			self.initx = self.initx + (self.ball.x - self.token[0]) * self.speed
			self.inity = self.inity + (self.ball.y - self.token[1]) * self.speed
			# print(f'{self.initx=}, {self.inity=}\n')
			overlap = self.GetOverlapBox()

			if overlap is not None:
				self.ball.godraw = False
				self.ball.dx = 0
				self.ball.dy = 0
				self.ball.t = 0
				self.ball.catch = True
				self.Bat = False
				if self.ball.bound == False:
					global sbo
					if(Out >= 3):
						ChangeAtt()
					pop()



				self.ball.initpos = copy.deepcopy([self.ball.x, self.ball.y])
				self.ball.drawpos = copy.deepcopy([self.ball.prevx, self.ball.prevy])
		else:
			if(self.num >= 2 and self.num < 7 and self.baseIndex < 4):
				print(f'{self.num=}: {self.baseIndex=}')



				if(abs(self.initx) >= self.base[self.baseIndex].x - 80 and abs(self.initx) <= self.base[self.baseIndex].x + 80
	   				and abs(self.inity) >= self.base[self.baseIndex].y - 80 and abs(self.inity) <= self.base[self.baseIndex].y + 80):
					self.base[self.baseIndex].InPlayer[1] = True
				else:
					self.base[self.baseIndex].InPlayer[1] = False
					self.initx += (self.base[self.baseIndex].x - self.initx) * self.speed
					self.inity += (self.base[self.baseIndex].y - self.inity) * self.speed

	def dist(self):
		x = (self.ball.initpos[0] + self.ball.dx) - self.initx
		y = (self.ball.initpos[1] + self.ball.dy) - self.inity

		return x ** 2 + y ** 2

	def update(self):
		global Score, ScoreIndex, Strike, Ballcount, Out, attackSequence
		self.move()

		if self.ball.t <= 1:
			self.dx -= (self.ball.dx * 0.01)
			self.dy -= (self.ball.dy * 0.01)
			# self.t = copy.deepcopy(self.ball.t)

		# self.x = self.initx - (self.ball.dx * self.ball.t)
		# self.y = self.inity - (self.ball.dy * self.ball.t)
		self.x = self.initx + self.dx
		self.y = self.inity + self.dy	


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
		






