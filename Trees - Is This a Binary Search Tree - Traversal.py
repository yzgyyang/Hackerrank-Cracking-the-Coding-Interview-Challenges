""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    arr = []
    find(arr, root)
    for i in range(1, len(arr)):
        if arr[i - 1] >= arr[i]:
            return False
    return True


def find(arr, node):
    if node.left:
        find(arr, node.left)
    arr += [node.data]
    if node.right:
        find(arr, node.right)

