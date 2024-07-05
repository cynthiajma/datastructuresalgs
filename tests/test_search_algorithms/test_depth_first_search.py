import unittest 
import os
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from search_algorithms.depth_first_search import *

class TestDepthFirstSearch(unittest.TestCase):
	def setUp(self):
		self.graph = {
		    'A': ['B', 'C'],
		    'B': ['A', 'D', 'E'],
		    'C': ['A', 'F'],
		    'D': ['B'],
		    'E': ['B', 'F'],
		    'F': ['C', 'E']
}

	def test_return_dfs_traversal(self):
		expected = ['A', 'C', 'F', 'E', 'B', 'D']
		result = return_dfs_traversal(self.graph, 'A')
		self.assertEqual(expected, result)

	def test_recursive_dfs_traversal(self):
		expected = ['A', 'C', 'F', 'E', 'B', 'D']
		result = return_dfs_traversal(self.graph, 'A')
		self.assertEqual(expected, result)



if __name__ == "__main__":
    unittest.main()