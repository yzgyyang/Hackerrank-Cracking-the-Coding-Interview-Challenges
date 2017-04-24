""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

INT_MIN = -4294967296
INT_MAX = 4294967296

def check_binary_search_tree_(root):
    return find(root, INT_MIN, INT_MAX)


def find(node, nmin, nmax):
    if not node:
        return True
    if node.data <= nmin or node.data >= nmax:
        return False
    return find(node.left, nmin, node.data) and find(node.right, node.data, nmax)

