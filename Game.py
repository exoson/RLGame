import cv2
import numpy as np
import math
import random
class Myrkky:
	def __init__(self):
		randomX = random.random()
		randomY = random.random()
		self.x = randomX * 1280
		self.y = randomY * 720
class Karkki:
	def __init__(self):
		randomX = random.random()
		randomY = random.random()
		self.x = randomX * 1280
		self.y = randomY * 720
class Game:
	RAD = 30
	FOODRAD = 10
	def __init__(self):
		self.x = 0
		self.y = 0
		self.rot = 0
		self.foods = []
		self.potion = []
	def forward(self):
		self.x += 10*math.cos(self.rot)
		self.y += 10*math.sin(self.rot)
		print self.x
		print self.y
	def turn(self,amt):
		self.rot += amt
	def update(self):
		randomPot = random.random()
		randomKark = random.random()
		keep = []
		keepotion = []
		if randomPot > 0.99:
			self.potion.append(Myrkky())
		if randomKark > 0.99:
			self.foods.append(Karkki())
		for ruoka in self.foods:
			if not (math.sqrt(math.pow(self.x-ruoka.x,2)+math.pow(self.y-ruoka.y,2)) < self.RAD + self.FOODRAD):
				keep.append(ruoka)
		for pot in self.potion:
			if not (math.sqrt(math.pow(self.x-pot.x,2)+math.pow(self.y-pot.y,2)) < self.RAD + self.FOODRAD):
				keepotion.append(pot)
		self.foods = keep
		self.potion = keepotion
		foodCounter = len(keep)
		potionCounter = len (keepotion)
		print foodCounter
		print potionCounter
	def render(self):
		view = np.zeros((720,1280,3),np.uint8)
		cv2.circle(view,(int(self.x),int(self.y)),self.RAD,(0,255,255))
		for ruoka in self.foods:
			cv2.circle(view,(int(ruoka.x), int(ruoka.y)),self.FOODRAD,(255,0,0))
		for potion in self.potion:
			cv2.circle(view,(int(potion.x), int(potion.y)),self.FOODRAD,(0,255,0))
		cv2.imshow('saas',view)
