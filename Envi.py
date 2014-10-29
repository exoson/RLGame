from pybrain.rl.environments import Environment
from Game import Game
import numpy as np
class env(Environment):
	discreteStates = False
	reward = 0
	game = Game()
	def getSensors(self):
		return env.game.getView(0)
	def performAction(self,action):
		if action[0] == 1:
			env.game.turn(0,0.1)
		if action[1] == 1:
			env.game.turn(0,-0.1)
		env.game.forward()
		env.game.update()
	def reset(self):
		print 'sees'