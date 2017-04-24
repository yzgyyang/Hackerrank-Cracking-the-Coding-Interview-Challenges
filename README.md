# Hackerrank - Cracking the Coding Interview Challenges

My solutions and thoughts to the practice problem set [Cracking the Coding Interview Challenges](https://www.hackerrank.com/domains/tutorials/cracking-the-coding-interview).

## [Arrays: Left Rotation](https://www.hackerrank.com/challenges/ctci-array-left-rotation)

**Brief Introduction:** Given an array of integers and a number, perform left rotations on the array.

**Solution:**  

Super easy problem with the following steps:  
1. Create a new array to store the result;
2. Copy a[0] ~ a[d - 1] elements to rotated[n - d];
3. Copy a[d] ~ a[n - 1] elements to rotated[0];
4. Return the new array.

Extremely easy problem with Python slices:  
```python
def array_left_rotation(a, n, k):
    return a[k:] + a[:k]
```

[Code](Arrays_Left_Rotation_Solution.py)


## [Trees - Is This a Binary Search Tree](https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/)

**Brief Introduction:** Decide if a tree is a BST.

**Concept:** A binary search tree (BST) is a node based binary tree data structure which has the following properties.
- The left subtree of a node contains only nodes with keys less than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- Both the left and right subtrees must also be binary search trees.

**Solution:**  

In a search tree, in-order traversal retrieves data in sorted order. So we perform an in-order traversal on the targeted tree, then check if the result is a sorted list.

In-order Traversal Function:
```python
def find(arr, node):
    if node.left:
        find(arr, node.left)
    arr += [node.data]
    if node.right:
        find(arr, node.right)
```

[Code](Trees_Is_This_a_Binary_Search_Tree_Traversal.py)


To improve efficiency, we set a max/min value for each child, so the program doesn't have to travel the full length if it's not a BST, and storing all the value into a list won't be necessary. 

```python
def find(node, nmin, nmax):
    if not node:
        return True
    if node.data <= nmin or node.data >= nmax:
        return False
    return find(node.left, nmin, node.data) and find(node.right, node.data, nmax)

find(root, INT_MIN, INT_MAX)
```

[Code](Trees_Is_This_a_Binary_Search_Tree_Solution.py)

