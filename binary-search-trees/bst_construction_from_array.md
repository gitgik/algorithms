### Construct a Min Height BST
Given an sorted array of integers, construct a min-height Binary Search Tree and return the root. All the BST rules apply.

```
Sample input:
    [1, 2, 3, 5, 10, 12, 15, 20, 24]
  
Sample output:
              10
            /    \
          2        15
         / \      /  \
         1  3     12  20
             \          \ 
             5          24
```


```python
# First Approach
def bst_constructor(A):
    """Complexity
        O(N log N) time where N is the total number of elements in the array
        O(N) space
    """
    if len(A) == 1:
        return BST(A[0])
    
    return bst_helper(A, None, 0, len(A) - 1)

def bst_helper(A, bst, start, end):
    # base case
    if start > end:
        return
    else:
        mid = (start + end) // 2
        value_to_add = A[mid]
        if bst is None:
            # create the root
            bst = BST(value_to_add)
        else:
            bst.insert(value_to_add)
        bst_helper(A, bst, start, mid - 1)
        bst_helper(A, bst, mid + 1, end)
    return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        if value_to_add < self.value:
            if self.left is None:
                self.left = BST(value_to_add)
            else:
                self.left.insert(value_to_add)
        else:
            if self.right is None:
                self.right = BST(value_to_add)
            else:
                self.right.insert(value_to_add)

```


```python
# Second approach
def bst_constructor(array):
    """O(n) time | O(n) space"""
    return bst_constructor_helper(array, None, 0, len(array) - 1)

def bst_constructor_helper(array, bst, start_index, end_index):
    if end_index < start_index:
        return
    else:
        mid_index = (start_index + end_index) // 2
        new_bst_node = BST(array[mid_index]) 
        if bst is None:
            bst = new_bst_node
        else:
            if array[mid_index] < bst.value:
                bst.left = BST(array[mid_index])
                bst = bst.left
            else:
                bst.right = BST(array[mid_index])
                bst = bst.right
        
        bst_constructor_helper(array, bst, start_index, mid_index - 1)
        bst_constructor_helper(array, bst, mid_index + 1, end_index)
        return bst
```


```python
# Third approach
def bst_construct(A):
    """O(n) time | O(n) space"""
    return bst_construct_helper(A, 0, len(A) - 1)

def bst_construct_helper(A, start, end):
    # base case
    if end < start:
        return None
    mid = (start + end) // 2
    bst = BST(A[mid])
    bst.left = bst_construct_helper(A, start, mid - 1)
    bst.right = bst_construct_helper(A, mid + 1, end)
    return bst

```


```python
root = bst_construct([1, 2, 4])
print(f"{root.value}, {root.left.value}, {root.right.value}")
```

    2, 1, 4



```python
root = bst_construct([1, 2, 3, 5, 10, 12, 15, 20, 24])
```


```python
root.left.left.value
```




    1




```python
# Fourth Appraoch: Cleanest
def bstConstruct(A):
    if not A:
        return None
    mid = len(A) // 2
    root = BST(A[mid])
    root.left = bstConstruct(A[:mid])
    root.right = bstConstruct(A[mid+1:])
    return root
```


```python
root = bstConstruct([1, 2, 3, 4, 5, 6, 7])

def inOrder(node):
    if not node:
        return
    inOrder(node.left)
    print(node.value)
    inOrder(node.right)

inOrder(root)
```

    1
    2
    3
    4
    5
    6
    7



```python

```
