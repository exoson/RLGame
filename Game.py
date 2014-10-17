import cv2
import numpy as np
import math
import random as rng

class Game:
	RAD = 20
	SHOTRAD = 7
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