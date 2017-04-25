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

**Solutions:**  

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


## [Tries: Contacts](https://www.hackerrank.com/challenges/ctci-contacts)

**Brief Introduction:** Find the number of strings which start with the given partial string.

**Concept:** A trie, also called radix tree or prefix tree (as they can be searched by prefixes), is a kind of search tree that is used to store strings. All the descendants of a node have a common prefix of the string associated with that node. Values tend only to be associated with leaves.
![Example of a Trie](img/Trie.png)

**Solutions:**

The initial thought is to use a nested for loop with O(n^2) complexity. It's correct, but exceeds the time limit.

```python
count = 0
for item in s:
    m = min(len(contact), len(item))
    if contact[:m] == item[:m]:
        count += 1
```

[Code](Tries_Contacts_O(N^2).py)


We implement a trie to achieve O(n*length). There are many ways to implement a trie. In Python, I found that the simplest way is to use nested dictionaries (they might become cumbersome or space inefficient for larger tries, but that's a good start). Something like:

```python
{'b': {'a': {'r': {'_': '_', 'z': {'_': '_'}}, 
             'z': {'_': '_'}}}, 
 'f': {'o': {'o': {'_': '_'}}}}
```

The ending of each word will have a key `'_'` with value `'_'` (they can be something else). So it traverses to the node of the last character of the given prefix and recursively checked for and counted words in the children. We find a word each time we reach a `'_'`.

```python
def trie_find(s, t):
    if len(s) == 0:
        return t
    if s[0] not in t:
        return {}
    return trie_find(s[1:], t[s[0]])


def trie_count_node(t):
    if not isinstance(t, dict):
        return 0
    ans = 0
    if '_' in t:
        ans += 1
    for key, value in t.items():
        ans += trie_count_node(value)
    return ans
```

[Code](Tries_Contacts_Trie.py)

It seems to be efficient enough, but it still got timeout. Why? My orginal sub-optimal solution might be nessesary if the question asked for the names under a node; however, since it only wants the count, it's more effecient to store the count in the trie node inclusively.

Now we insert a `t['_'] = count_of_the_words_contained` in each node. Once it finds the starting node, it just prints out `t['_']` of that node.

```python
def trie_insert(s, t):
    if '_' not in t:
        t['_'] = 0
    t['_'] += 1
    if len(s) == 0:
        return
    if s[0] not in t:
        t[s[0]] = {}
    trie_insert(s[1:], t[s[0]])
```

[Code](Tries_Contacts_Solution.py)

It passed the tests.
