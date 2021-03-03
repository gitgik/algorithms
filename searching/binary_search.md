```python
def binary_search(array, target):
    """
    An iterative implementation of binary search. 
    (recursive takes extra space, so solving it iteratively is better -- constant space.)

    Returns index of the target if found
    or -1 if it isn't.

    Complexity:
        O(log (n)) time - since  we split the search space by half every time
                          we shift the left or right indexes.
        O(1) space
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        if target == array[middle]:
            return middle
        elif target < array[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def recursive_binary_search(array, target):
    """
    A recursive approach to implementing binary search algorithm.

    NOTE: Less efficient when it comes to space complexity.
    Compexity:
        O(log(n)) time
        O(log (n)) space.
    """
    return binary_search_helper(array, target, 0, len(array) - 1)


def binary_search_helper(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    potential_match = array[middle]

    if target == potential_match:
        return middle
    elif target < potential_match:
        return binary_search_helper(array, target, left, middle - 1)
    else:
        return binary_search_helper(array, target, middle + 1, right)
```


```python

```
