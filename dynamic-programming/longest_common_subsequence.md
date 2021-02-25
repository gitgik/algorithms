## Problem

Write a function that takes two strings and returns their longest common subsequence.

A subsequence is a set of characters in a string that aren't necessarily adjacent to each other but are in the same order that they appear in the string.

For example, given string `abcd`, `acd` is a subsequence.




```python
def longestCommonSubsequence(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # create a 2-dim array from the strings
    array = [[[] for j in range(n + 1)] for i in range(m + 1)]
    
    # iterate through the 2D array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # compare the string characters together for equality
            if str1[i - 1] == str2[j - 1]:
                # Concatenate A[i - 1][j - 1] with A[i][j]
                array[i][j] = array[i - 1][j - 1] + [str1[i - 1]]
            else:
                # A[i][j] = Max(A[i-1][j], A[i][j-1])
                array[i][j] = max(array[i - 1][j], array[i][j - 1], key=len)
    # return the bottom-rightmost element of the 2D array
    return array[-1][-1]

    # O(M * N ) * O(min(m, n)) ===> O(MN * min(M, N))  == Space complexity
    
    
```


```python
longestCommonSubsequence("ZXVVYXW", "XKYKZFW")
```




    ['X', 'Y', 'W']




```python

```
