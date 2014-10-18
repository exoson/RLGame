import cv2
import numpy as np
import math
import random
class Myrkky:
        def __init__(self):
                random = random.random()
                randomY = random.random
                self.x = random
                self.y = randomY
class Karkki:
        def __init__(self):
                random = random.random()
                randomY = random.random()
                self.x = random * 100
                self.y = randomY * 100
class Game:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.rot = 0
		foods = []
		potion = []
	def forward(self):
		self.x += 10*math.cos(self.rot)
		self.y += 10*math.sin(self.rot)
		print self.x
		print self.y
	def turn(self,amt):
		self.rot += amt
	def update(self):
                random = random.random()
                randomKark = random.random()
                keep = []
                keepotion = []
                if random > 0.99:
                        potion.append(myrkky)
                if randomKark > 0.99:
                        foods.append(karkki)
                if not (math.sqrt(math.pow(self.x-ruoka.x),2)+(math.pow(self.y-ruoka.y),2)) < 10:
                        keep.append[karkki]
                if not (math.sqrt(math.pow(self.x-potion.x),2)+(math.pow(self.y-potion.y),2)) < 10:
                        keepotion.append[myrkky]
                foods = keep
                keepotion = potion
                foodCounter = len(keep)
                potionCounter = len (keepotion)
                print foodCounter
                print potionCounter
	def render(self):
		view = np.zeros((720,1280,3),np.uint8)
		cv2.circle(view,(int(self.x),int(self.y)),100,(0,255,255))
		for ruoka in self.foods:
                        cv2.circle(view,(ruoka.x, ruoka.y),10,(255,0,0))
                for potion in self.potion:
                        cv2.circle(view,(potion.x, potion.y),10,(0,255,0))
		cv2.imshow('saas',view)
