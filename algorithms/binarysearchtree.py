
class BinaryNode:

    def __init__(self, value = None):
        """Create binary node"""
        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        """Adds a new node to the tree containing this value"""
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)


class BinaryTree:

    def __init__(self):
        """Create empty binary tree"""
        self.root = None
        
    def add(self, value):
        """Insert value into proper location in Binary Tree"""
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def contains(self, target):
        """Check whether BST contains target value"""

        node = self.root
        while node:
            if target == node.value:
                return True
            if target < node.value:
                node = node.left
            else:
                node = node.right
                
        return False
