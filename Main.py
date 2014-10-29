
from pybrain.rl.learners.valuebased import ActionValueNetwork
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q, SARSA
from pybrain.rl.experiments import Experiment
from pybrain.rl.environments import Task
from Game import Game
from Envi import env
from Taski import Taski
import cv2

class Main:
	UP = 119
	LEFT = 97
	RIGHT = 100
	SPACE = 32
	game = Game()
	def getInput(self):
		key = cv2.waitKey(1)
		print key
		if key == self.UP:
			self.game.forward(0)
		if key == self.LEFT:
			self.game.turn(0,-0.1)
		if key == self.RIGHT:
			self.game.turn(0,0.1)
		if key == self.SPACE:
			self.game.shoot(0)
	def update(self):
		self.game.update()
	def render(self):
		self.game.render()
	def run(self):
		self.running = True
		while self.running:
			self.getInput()
			self.update()
			self.render()
	def train(self):
		environment = env()
		net = ActionValueNetwork(3,3)
		learner = Q()
		agent = LearningAgent(net,learner)
		task = Taski(environment)
		exp = Experiment(task,agent)
		self.training = True
		while self.training:
			exp.doInteractions(100)
			agent.learn()
			agent.reset()
			
			environment.game.render()
if __name__ == '__main__':
	main = Main()
	main.train()