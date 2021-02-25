## Mergesort
Implement mergesort.

### Approach
Mergesort is a divide-and-conquer algorithm. We divide the array into two sub-arrays, recursively call the function and pass in the two halves, until each sub-array has one element. Since each sub-array has only one element, they are all sorted. We then merge each sub-array until we form a sorted array.

The merge function will be used to merge two sorted halves.


```python
def merge_sort(array, left, right):
    if left < right:
        mid = (left + (right - 1)) // 2   # same as ((left + right) // 2) but avoids overflow for large left
    
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)
    return array
```


```python
def merge(array, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    # create temp arrays
    left_array = [0] * n1
    right_array = [0] * n2
    
    # copy the data to the temp arrays
    for i in range(0, n1):
        left_array[i] = array[left + i]
    
    for j in range(0, n2):
        right_array[j] = array[mid + 1 + j]
    
    # merge the temp arrays into one array
    i = 0  # index for arr1
    j = 0  # index for arr2
    k = left  # index for the final array
    
    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1
    
    # copy remaining elements of left array if any
    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1
    
    # copy remaining elements of right array if any
    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1
```


```python
A = [2, 4, 1, 6, 0, 3]
n = len(A)
merge_sort(A, 0, n - 1)
```




    [0, 1, 2, 3, 4, 6]



## Bottom-up approach
We can implement merge-sort iteratively in a bottom-up manner. 

We start by sorting all sub-arrays of size 1, then we merge them into sub-arrays of two elements. We perform successive merges until the array is completely sorted. 




```python
def merge(A, temp, frm, mid, to):
    k = frm
    i = frm
    j = mid + 1
    
    while i <= mid and j <= to:
        if A[i] <= A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            j += 1
        k += 1
        
    # copy remaining elements
    while i < len(A) and i <= mid:
        temp[k] = A[i]
        i += 1
        k += 1
    
    # no need to copy second half ...
    
    # copy back original list to reflect sorted order
    for i in range(frm, to + 1):
        A[i] = temp[i]
    
def mergeSort(array):
    left = 0
    right = len(array) - 1
    temp = array.copy()
    
    m = 1
    while m <= right - left:
        for i in range(left, right, 2 * m):
            frm = i
            mid = i + m - 1
            to = min(i + 2 * m - 1, right)
            merge(A, temp, frm, mid, to)
        m = 2 * m
    return array

```


```python
A = [5, -4, 3, 2, 1]
mergeSort(A)
```




    [-4, 1, 2, 3, 5]




```python

```
