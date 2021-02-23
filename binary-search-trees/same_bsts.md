## Problem
An array of integers represents a Binary Search Tree(BST) obtained by inserting each integer into the array (from left to right) into the BST. 

Without constructing a BST tree, write a function that returns a boolean indicating whether the two arrays represent the same BST.

A BST tree is a tree that consists of only BST nodes. A node is said to be a BST node if it meets the BST property: its value is strictly greater than the values of the every node to its left; its value is less or equal to the nodes to its right, and its children nodes are also BST nodes or Null values.

Sample input: 
```python
[10, 15, 8, 12, 92, 81, 5, 2, 11]

[10, 8, 5, 15, 2, 12, 11, 94, 81]
```

Sample output: 
```
True
```


```python
## Solution 1
## Time: O(n**2) | O(n**2), where n is the length of an input array

def is_same_bst(arr_1, arr_2):
    if len(arr_1) != len(arr_2):
        return False
    
    if len(arr_1) == 0 and len(arr_2) == 0:
        return True
    
    if arr_1[0] != arr_2[0]:
        return False
    
    left_subtree_1 = get_smaller(arr_1)
    left_subtree_2 = get_smaller(arr_2)
    right_subtree_1 = get_bigger_or_equal(arr_1)
    right_subtree_2 = get_bigger_or_equal(arr_2)
    
    return is_same_bst(left_subtree_1, left_subtree_2) and is_same_bst(right_subtree_1, right_subtree_2)
    

def get_smaller(array):
    node = array[0]
    # from the second index onwards (array[1:]) ... check BST property against array[0]
    smaller = [i for i in array[1:] if i < node]
    return smaller

def get_bigger_or_equal(array):
    node = array[0]
    # from the second index onwards (array[1:]) ... check BST property against array[0]
    bigger = [i for i in array[1:] if i >= node]
    return bigger
    
```


```python
array_1 = [10, 15, 12, 94]
array_2 = [10, 15, 12, 94]
is_same_bst(array_1, array_2)
```




    True



## Improving on previous solution
We can improve the space complexity of $O(n^{2})$ by using index pointers to get rid of storing the arrays.

It's a little confusing and a lot less readable than the first solution but far optimal than the first. :)


```python
# solution 2: more efficient
# Time: O(n2) | O(d), where d == depth of the BST, while n == length of each input array
def same_bst(a, b):
    """
    a and b are arrays representing the two BSTs
    """
    if len(a) != len(b):
        return False
    
    return are_same_bsts(a, b, 0, 0, float("-inf"), float("inf"))
 

def are_same_bsts(a, b, a_root_index, b_root_index, min_val, max_val):
    if a_root_index == -1 or b_root_index == -1:
        return a_root_index == b_root_index
    
    if a[a_root_index] != b[b_root_index]:
        return False
    
    left_root_index_a = get_index_smaller(a, a_root_index, min_val)
    left_root_index_b = get_index_smaller(b, b_root_index, min_val)
    right_root_index_a = get_index_bigger_or_equal(a, a_root_index, max_val)
    right_root_index_b = get_index_bigger_or_equal(b, b_root_index, max_val)
    
    current_value = a[a_root_index]
    left_are_same = are_same_bsts(
        a, b, left_root_index_a, left_root_index_b, 
        min_val=min_val, 
        max_val=current_value
    )
    right_are_same = are_same_bsts(
        a, b, right_root_index_a, right_root_index_b, 
        min_val=current_value, 
        max_val=max_val
    )
    return left_are_same and right_are_same


def get_index_smaller(array, starting_index, min_val):
    # Find the index of the first smaller value after the starting index.
    # If it's less than the min value, it exists to the left subtree of the parent node
    for i in range(starting_index + 1, len(array)):
        if array[i] < array[starting_index] and array[i] >= min_val:
            return i
    return -1


def get_index_bigger_or_equal(array, starting_index, max_val):
    # Find the index of the first bigger/equal value after the starting index. 
    # If it is greater than the max value, it exists to the right subtree of the parent node.
    for i in range(starting_index + 1, len(array)):
        if array[i] >= array[starting_index] and array[i] < max_val:
            return i
    return -1
    
```


```python
same_bst([10, 15, 8, 12, 94, 80, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 80])
```




    True




```python
import unittest

class SameBSTTestCase(unittest.TestCase): 
    def test_same_bst(self):
        array_one = list(range(10))
        array_two = list(range(10))
        self.assertEqual(same_bst(array_one, array_two), True)
    
    def test_different_bst(self):
        array_one = list(range(10))
        array_two = [12, 1, 4, 5, 2, 3, 6, 8, 8]
        self.assertEqual(same_bst(array_one, array_two), False)
        
    def test_differently_ordered_bst_but_same(self):
        array_one, array_two = [10, 15, 8, 12, 94, 80, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 80]
        self.assertEqual(same_bst(array_one, array_two), True)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```
