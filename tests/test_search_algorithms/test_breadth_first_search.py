import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from search_algorithms.breadth_first_search import *
from collections import deque



class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        # Set up the binary tree for testing
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)
        self.root.right.right = TreeNode(6)

        self.sym_root = TreeNode(1)
        self.sym_root.left = TreeNode(2)
        self.sym_root.right = TreeNode(2)
        self.sym_root.left.left = TreeNode(3)
        self.sym_root.left.right = TreeNode(4)
        self.sym_root.right.left = TreeNode(4)
        self.sym_root.right.right = TreeNode(3)

        # Set up the graph for testing
        self.graph = {
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "F"],
            "D": ["B"],
            "E": ["B", "F"],
            "F": ["C", "E"],
        }

    def test_level_order(self):
        expected = [[1], [2, 3], [4, 5, 6]]
        result = level_order(self.root)
        self.assertEqual(result, expected)

    def test_symmetry_check(self):
        self.assertTrue(symmetry_check(self.sym_root))

        asym_root = TreeNode(1)
        asym_root.left = TreeNode(2)
        asym_root.right = TreeNode(2)
        asym_root.left.right = TreeNode(None)
        asym_root.right.right = TreeNode(3)
        asym_root.right.right = TreeNode(None)
        asym_root.right.right = TreeNode(3)
        self.assertFalse(symmetry_check(asym_root))

    def test_enqueue(self):
        queue = deque()
        enqueue(queue, 10)
        self.assertEqual(list(queue), [10])

    def test_dequeue(self):
        queue = deque([10])
        result = dequeue(queue)
        self.assertEqual(result, 10)
        self.assertEqual(list(queue), [])

    def test_peek(self):
        queue = deque([10])
        result = peek(queue)
        self.assertEqual(result, 10)

    def test_return_bfs_traversal(self):
        expected = ["A", "B", "C", "D", "E", "F"]
        result = return_bfs_traversal(self.graph, "A")
        self.assertEqual(result, expected)

    def test_return_shortest_path(self):
        expected = ["A", "C", "F"]
        result = return_shortest_path(self.graph, "A", "F")
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
