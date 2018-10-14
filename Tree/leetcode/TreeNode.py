# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
