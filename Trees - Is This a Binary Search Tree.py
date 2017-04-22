""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check_binary_search_tree_(root):
    arr = find([], root)
    for i in range(1, len(arr)):
        if arr[i - 1] >= arr[i]:
            return False
    return True


def find(arr, node):
    if node.left:
        find_node(arr, node.left)
    arr += [node.data]
    if node.right:
        find_node(arr, node.right)
    return arr

        
def find_node(arr, node):
    if node.left:
        find_node(arr, node.left)
    arr += [node.data]
    if node.right:
        find_node(arr, node.right)
