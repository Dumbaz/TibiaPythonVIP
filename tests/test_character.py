import unittest
from character import Character

class CharacterTest(unittest.TestCase):
	"""General Character Test"""
	def test_creation(self):
		Satai = Character('Satai', 'Master Sorcerer', '95', 'Rowana', 'Jul 10 2015, 13:05:56 CEST', 'Premium Account')
		self.assertEqual(Satai.name, "Satai")

if __name__ == '__main__':
    unittest.main()

# print Satai.time

# print Satai.level
# Satai.updateLevel(100)
# print Satai.level

# Satai.updateName('kurwa')
# print Satai.name

# Satai.updateWorld('Kenora')
# print Satai.world

# Satai.updateAccStatus('Free Account')
# print Satai.accStatus

# print Satai.time