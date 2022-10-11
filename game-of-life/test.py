import unittest
from main import *

class TestGameOfLife(unittest.TestCase):
	def setUp(self):
		unis = []
		files = ['input1.txt', 'input2.txt', 'input3.txt']
		for item in files:
			f = open('test-inputs/' + item, 'r')
			data = f.read()
			f.close()
			unis.append(create_universe(data))
		self.uni1, self.uni2, self.uni3 = unis

	def test_universe(self):
		self.assertEqual(self.uni1.gens, 4)
		self.assertEqual(self.uni1.cols, 8)
		self.assertEqual(self.uni1.rows, 5)
		self.assertEqual(
			self.uni1.field, 
			[
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['x', '.', '.', '.', '.', '.', '.', '.'], 
				['x', '.', '.', '.', '.', '.', '.', '.'], 
				['x', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.']
			]
		)

		self.assertEqual(self.uni2.gens, 3)
		self.assertEqual(
			self.uni2.field, 
			[
				['x', 'x', '.', '.', '.', '.', '.', 'x'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.']
			]
		)

		self.assertEqual(self.uni3.gens, 5)
		self.assertEqual(
			self.uni3.field, 
			[
				['.', '.', '.', '.', '.', '.', '.', 'x'], 
				['.', '.', '.', '.', '.', '.', '.', 'x'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', 'x']
			]
		)

	def test_neighbours(self):
		result = neighbours(self.uni1, 1, 2)
		self.assertEqual(result, 3)

		result = neighbours(self.uni1, 7, 3)
		self.assertEqual(result, 2)

		result = neighbours(self.uni1, 0, 0)
		self.assertEqual(result, 1)

		result = neighbours(self.uni1, 3, 3)
		self.assertEqual(result, 0)

		result = neighbours(self.uni2, 0, 1)
		self.assertEqual(result, 3)

		result = neighbours(self.uni3, 0, 4)
		self.assertEqual(result, 2)

	def test_cell_change(self):
		result = cell_change('.', 2)
		self.assertEqual(result, '.')

		result = cell_change('.', 3)
		self.assertEqual(result, 'x')

		result = cell_change('.', 4)
		self.assertEqual(result, '.')

		result = cell_change('x', 1)
		self.assertEqual(result, '.')

		result = cell_change('x', 2)
		self.assertEqual(result, 'x')

		result = cell_change('x', 4)
		self.assertEqual(result, '.')

	def test_next_gen(self):
		result = next_gen(self.uni1)
		self.assertEqual(
			result, 
			[
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['x', 'x', '.', '.', '.', '.', '.', 'x'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.']
			]
		)

		result = next_gen(self.uni2)
		self.assertEqual(
			result, 
			[
				['x', '.', '.', '.', '.', '.', '.', '.'], 
				['x', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['x', '.', '.', '.', '.', '.', '.', '.']
			]
		)

		result = next_gen(self.uni3)
		self.assertEqual(
			result, 
			[
				['x', '.', '.', '.', '.', '.', 'x', 'x'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.']
			]
		)

	def test_evolution(self):
		evolution(self.uni1)
		self.assertEqual(
			self.uni1.field, 
			[
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['x', '.', '.', '.', '.', '.', '.', '.'], 
				['x', '.', '.', '.', '.', '.', '.', '.'], 
				['x', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.']
			]
		)

		evolution(self.uni2)
		self.assertEqual(
			self.uni2.field, 
			[
				['x', '.', '.', '.', '.', '.', '.', '.'], 
				['x', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['x', '.', '.', '.', '.', '.', '.', '.']
			]
		)

		evolution(self.uni3)
		self.assertEqual(
			self.uni3.field, 
			[
				['x', '.', '.', '.', '.', '.', 'x', 'x'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.'], 
				['.', '.', '.', '.', '.', '.', '.', '.']
			]
		)


unittest.main()
