import cv2
import numpy as np
import math
class Game:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.rot = 0
	def forward(self):
		self.x += 10*math.cos(self.rot)
		self.y += 10*math.sin(self.rot)
		print self.x
		print self.y
	def turn(self,amt):
		self.rot += amt
	def update(self):
		print 'sus'
	def render(self):
		view = np.zeros((720,1280,3),np.uint8)
		cv2.circle(view,(int(self.x),int(self.y)),100,(250,175,190))
		cv2.imshow('saas',view)