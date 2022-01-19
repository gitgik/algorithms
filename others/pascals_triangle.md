## Pascals Triangle

A Pascal's triangle is a triangular array of integers contructed as follows:
- First row consists of number 1
- For each row below it, each element is the sum of the numbers directly above it, on either side.

For example:
```
        1
      1   1
    1   2   1
  1  3    3   1
1  4   6    4   1
```

Given k, return kth row of the triangle



### Solution 1
We can make the triangle a right angle to simplify the problem.
```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```
Initialize a k by k array, iterate through each row, setting each value to be the sum of its top and top-left values


```python
def pascal(k):
    rows = [[0 for i in range(k)] for _ in range(k)]
    
    rows[0][0] = 1
    
    for i in range(1, k):
        for j in range(i + 1):
            rows[i][j] = rows[i - 1][j] + rows[i - 1][j - 1] 
    
    return rows[-1]

```


```python
pascal(5)
```




    [1, 4, 6, 4, 1]



### Solution 2
The above solution takes O(k^2) time and space.
We can solve in O(k) space.

Consider a row, say k = 3 and preceded and appended with a zero: [0, 1, 3, 3, 1, 0]. It turns out that working out backwards through this row, incrementing each value by that of its left neighbor will give us a solution.

For example for row [0, 1, 3, 3, 1, 0], we will perform the following operations:
- replace right-most 0 with 0 + 1 = 1
- replace 1 with 1 + 3 = 4
- replace 3 with 3 + 3 = 6
- replace 3 with 3 + 1 = 4
- replace 1 with 1 + 0 = 1

The resulting row will be [0, 1, 4, 6, 4, 1], and the first element will remain untouched (zero).
After doing this k times, we return the row with the first element (zero) removed.



```python
def pascal_triangle(k):
    row = [0 for _ in range(k + 1)]
    row[1] = 1
    
    for i in range(1, k + 1):
        for j in range(i, 0, -1):
            row[j] += row[j - 1]
            
    return row[1:]

```


```python
pascal_triangle(k=6)
```




    [1, 5, 10, 10, 5, 1]




```python

```
