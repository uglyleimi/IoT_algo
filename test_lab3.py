import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def test_create_node(self):
        node = BinaryTree(5)
        self.assertEqual(node.val, 5)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_load_from_file(self):
        root = BinaryTree.load_from_file("tree.txt")
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
        self.assertEqual(root.left.right.val, 5)
        self.assertEqual(root.right.left.val, 6)
        self.assertEqual(root.right.right.val, 7)

    def test_null_nodes(self):
        root = BinaryTree.load_from_file("tree.txt")
        # вузол 5 не має дітей
        self.assertIsNone(root.left.right.left)
        self.assertIsNone(root.left.right.right)

    def test_invert_root(self):
        root = BinaryTree.load_from_file("tree.txt")
        root.invert_tree()
        self.assertEqual(root.left.val, 3)
        self.assertEqual(root.right.val, 2)

    def test_invert_second_level(self):
        root = BinaryTree.load_from_file("tree.txt")
        root.invert_tree()
        self.assertEqual(root.left.left.val, 7)
        self.assertEqual(root.left.right.val, 6)
        self.assertEqual(root.right.left.val, 5)
        self.assertEqual(root.right.right.val, 4)

    def test_invert_twice(self):
        root = BinaryTree.load_from_file("tree.txt")
        root.invert_tree()
        root.invert_tree()
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
        self.assertEqual(root.left.right.val, 5)


if __name__ == "__main__":
    unittest.main()
