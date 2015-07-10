import time

class Character(object):
	"""A Tibia Character"""
	def __init__(self, name, vocation, level, world, lastlogin, accStatus):
		super(Character, self).__init__()
		self.name = [name]
		self.vocation = vocation
		self.level = [level]
		self.world = [world]
		self.lastLogin = [lastlogin]
		self.accStatus = [accStatus]
		self.time = [int(time.time())]
	def updateTime(self, newTime):
		self.time.insert(0, newTime)
	def updateName(self, newName):
		self.name.insert(0, [newName, self.time[0])
	def updateLevel(self, newLevel):
		self.level.insert(0, [newLevel, self.time[0]])
	def updateWorld(self, newWorld):
		self.world.insert(0, [newWorld, self.time[0]])
	def updateLastLogin(self, newLastLogin):
		self.lastlogin.insert(0, [newLastLogin, self.time[0]])
	def updateAccStatus(self, newAccStatus):
		self.accStatus.insert(0, [newAccStatus, self.time[0]])
	def updateUsualSuspects(self, newTime, newLevel, newLastLogin):
		updateTime(newTime)
		updateLevel(newLevel)
		updateLastLogin(newLastLogin)