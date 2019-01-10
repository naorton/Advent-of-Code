
import unittest
import puzzle

class TestBasic(unittest.TestCase):

	def test_pass(self):
		data = puzzle.parse("data.txt")
		answer = puzzle.solve(data)
		self.assertEqual(0, answer)

	def test_directionChanger(self):
		pass

	def test_northChanger(self):
		self.assertEqual(puzzle.northChanger("R"), "East")
		self.assertEqual(puzzle.northChanger("L"), "West")

	def test_eastChanger(self):
		self.assertEqual(puzzle.eastChanger("R"), "South")
		self.assertEqual(puzzle.eastChanger("L"), "North")

	def test_southChanger(self):
		self.assertEqual(puzzle.southChanger("R"), "West")
		self.assertEqual(puzzle.southChanger("L"), "East")

	def test_westChanger(self):
		self.assertEqual(puzzle.westChanger("R"), "North")
		self.assertEqual(puzzle.westChanger("L"), "South")

if __name__ == '__main__':
	unittest.main()