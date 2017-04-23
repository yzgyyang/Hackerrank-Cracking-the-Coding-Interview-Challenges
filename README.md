# Hackerrank - Cracking the Coding Interview Challenges

My solutions and thoughts to the practice problem set [Cracking the Coding Interview Challenges](https://www.hackerrank.com/domains/tutorials/cracking-the-coding-interview).

## [Arrays: Left Rotation](https://www.hackerrank.com/challenges/ctci-array-left-rotation)

**Brief Introduction:** Given an array of integers and a number, perform left rotations on the array.

**Solution:** Super easy problem with the following steps:  
1. Create a new array to store the result;
2. Copy a[0] ~ a[d - 1] elements to rotated[n - d];
3. Copy a[d] ~ a[n - 1] elements to rotated[0];
4. Return the new array.

Extremely easy problem with Python slices:  
```python
def array_left_rotation(a, n, k):
    return a[k:] + a[:k]
```

*Took me 5 min.*

