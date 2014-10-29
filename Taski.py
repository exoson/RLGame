from pybrain.rl.environments.task import Task
class Taski(Task):
	def getReward():
		return self.env.game.getReward(0)