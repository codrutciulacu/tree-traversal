import unittest
from unittest.mock import patch

from tree import Tree

class TestFindTree(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.empty_tree = Tree()
        tree = Tree()
        tree.add(11)
        tree.add(9)
        tree.add(8)
        tree.add(7)
        tree.add(3)
        tree.add(5)
        tree.add(14)
        self.not_empty_tree = tree

    def test_empty_tree(self):
        returned_val = self.empty_tree.find(3)
        self.assertIsNone(returned_val)
        
    def test_non_empty_tree(self):
        returned_val = self.not_empty_tree.find(3)
        self.assertIsNotNone(returned_val)
        self.assertEqual(3, returned_val.data)
if __name__ == '__main__':
    unittest.main()