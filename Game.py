import cv2
import numpy as np
import math
import random as rng

class Game:
	RAD = 20
	SHOTRAD = 7
	VDIST = 50
	def __init__(self):
		self.fighters = []
		self.fighters.append([100,100,0])
		self.fighters.append([500,500,0])
		self.shots = []
	def forward(self,fighter):
		self.fighters[fighter][0] += 10*math.cos(self.fighters[fighter][2])
		self.fighters[fighter][1] += 10*math.sin(self.fighters[fighter][2])
	def turn(self,fighter,amt):
		self.fighters[fighter][2] += amt
	def shoot(self,fighter):
		self.shots.append([self.fighters[fighter][0],self.fighters[fighter][1],self.fighters[fighter][2],fighter])
	def checkCollisions(self):
		keep = []
		for fighter in self.fighters:
			for shot in self.shots:
				if self.fighters[shot[3]] != fighter:
					if not (math.sqrt(math.pow(fighter[0]-shot[0],2)+math.pow(fighter[1]-shot[1],2)) < self.RAD):
						keep.append(shot)
					else:
						fighters[shot[3]]
		self.shots = keep;
	def update(self):
		self.checkCollisions()
		for shot in self.shots:
			shot[0] += 10*math.cos(shot[2])
			shot[1] += 10*math.sin(shot[2])
	def render(self):
		view = np.zeros((720,1280,3),np.uint8)
		cv2.circle(view,(int(self.fighters[0][0]),int(self.fighters[0][1])),self.RAD,(250,175,190),-1)
		cv2.circle(view,(int(self.fighters[1][0]),int(self.fighters[1][1])),self.RAD,(0,0,255),-1)
		for shot in self.shots:
			cv2.circle(view,(int(shot[0]),int(shot[1])),self.SHOTRAD,(0,128,255),-1)
		cv2.imshow('saas',view)
	def getView(self,fighter):
		sees = np.zeros((3),np.uint8)
		x0 = self.fighters[fighter]
		y0 = self.fighters[fighter]
		x1 = self.fighters[1][0]
		y1 = self.fighters[1][1]
		k1 = math.tan(self.fighters[fighter][2])
		k2 = k1 - math.PI/8
		k3 = k1 + math.PI/8
		k4 = y1-y0 / x1 - x0 if x1-x0 != 0 else abs(y1-y0)/y1-y0 * math.PI / 2
		a0 = math.atan(abs((k1-k4)/1 + k1*k4))
		a1 = math.atan(abs((k2-k4)/1 + k2*k4))
		a2 = math.atan(abs((k3-k4)/1 + k3*k4))
		d = math.sqrt((y1-y0) ** 2 + (x1-x0) ** 2)
		'''
		c1 = y0 - k1 * x0
		c2 = y0 - k2 * x0
		c3 = y0 - k3 * x0
		d1 = math.abs(k1 * x1 + y1 + c1)/math.sqrt(k ** 2 + 1)
		d2 = math.abs(k2 * x1 + y1 + c2)/math.sqrt(k ** 2 + 1)
		d3 = math.abs(k3 * x1 + y1 + c3)/math.sqrt(k ** 2 + 1)
		'''
		if d * math.sin(a0) < RAD:
			sees[1] = min(math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2),VDIST)
		if d * math.sin(a1) < RAD:
			sees[0] = min(math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2),VDIST)
		if d * math.sin(a2) < RAD:
			sees[2] = min(math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2),VDIST)
	def getReward(fighter):
		return 1