import time

class Character(object):
	"""A Tibia Character"""
	def __init__(self, name, vocation, level, world, last_login, account_status):
		super(Character, self).__init__()
		self.name = [name]
		self.vocation = vocation
		self.level = [int(level)]
		self.world = [world]
		self.last_login = [last_login]
		self.account_status = [account_status]
		self.time = [int(time.time())]
	def update_time(self, new_time):
		self.time.insert(0, new_time)
	def update_name(self, new_name):
		self.name.insert(0, [new_name, self.time[0]])
	def update_level(self, new_level):
		self.level.insert(0, [int(new_level), self.time[0]])
	def update_world(self, new_world):
		self.world.insert(0, [new_world, self.time[0]])
	def update_last_login(self, new_last_login):
		self.last_login.insert(0, [new_last_login, self.time[0]])
	def update_account_status(self, new_account_status):
		self.account_status.insert(0, [new_account_status, self.time[0]])
	def update_usual_suspects(self, new_time, new_level, new_last_login):
		update_time(new_time)
		update_level(new_level)
		update_last_login(new_last_login)
