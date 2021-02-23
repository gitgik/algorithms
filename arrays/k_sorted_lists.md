# Finding The Smallest Interval of K-sorted Lists.

Given K sorted lists of integers, return the **smallest interval** (inclusive) that contains at least one element from each least.

For example, given:

```python
[[0, 1, 4, 17, 20, 25, 31],
 [5, 6, 10],
 [0, 3, 7, 8, 12]]
```
The smallest range here is [3,5], since it contains:
* 4 from first list,
* 5 from the second list (inclusive),
* 3 from the third list (inclusive)



## Naive Solution
The brute force solution would be to compare every pair of elements in the lists and consider their intervals. After finding this interval, traverse every list to make sure that there is at least one element from each list in the interval.

In order to find the smallest such interval, we need to store the smallest seen so far, and update if we see a smaller interval.

This would be an expensive O(N^3), where N is the total number of elements in all K lists. On the bright side, this solution uses O(1) memory, since it only needs to store the current smallest interval.


## Solution 1: K-pointers
Since the K lists are all sorted, this suggest iterating from the beginning (smallest elements) to end (largest elements).

&nbsp;

Imagine comparing the minimum values of all the arrays: In our example above, the first values will be **[0, 5, 0]**. And the interval would be the minimum and maximum of these values: **[0, 5]**.

&nbsp;

This is one such interval but we aren't sure if it's the smallest. So we must keep looking. We must step along by increasing the minimum. In this case, the next interval we should consider is **[1, 5]**

Let's translate this process into an alogirithm:

1. Initialize K pointers, one for each list, pointing the minimum element in the list. (index 0 -- because they are sorted).
2. Initialize variables to track the right and left boundaries of the interval.
3. Find the pointer pointing to the **minimum** and the pointer pointing to the **maximum** of all the values pointed to. This becomes your **tracked interval**.
4. If the new interval is smaller than the previously tracked interval, update the tracked interval to be this new interval.
5. Increment the minimum value pointer. After incrementing this pointer, it may not point to a minimum value anymore.
6. Repeat steps 3 -5 until we get to the end of one of the lists.
7. Return the tracked interval (by now, it's the smallest)


```python
def smallest_interval(k_arrays):
    # step 1: init K pointers 
    k_pointers = [0] * len(k_arrays)  # evaluates to [0, 0, 0]
    # step 2: init the left, right boundaries of the interval
    interval = float('-inf'), float('inf')

    while True:
        # initialize local max and min, for updating tracked interval.
        local_max = float('-inf')
        local_min = float('inf')
        min_index = -1
        reached_end = False
        
        # step 3: find out which is the max, min to make the interval
        for i in range(len(k_pointers)):
            
            # first, check if we've reached the end of one of the K-lists
            if k_pointers[i] >= len(k_arrays[i]):
                reached_end = True
                break

            if k_arrays[i][k_pointers[i]] > local_max:
                local_max = k_arrays[i][k_pointers[i]]
            
            if k_arrays[i][k_pointers[i]] < local_min:
                local_min = k_arrays[i][k_pointers[i]]
                # save the index of minimum value, to be used later for incrementing
                min_index = i
        
        # if we've reached the end of any list,
        # we've already found the smallest interval
        if reached_end:
            break
            
        # step 4: update, if the new interval is < previous interval
        if local_max - local_min < interval[1] - interval[0]:
            interval = local_min, local_max
            
        # step 5: increment the minimum value pointer
        k_pointers[min_index] = k_pointers[min_index] + 1
            
    return interval

```


```python
# let's test it out
k_arrays = [[0, 1, 4, 17, 20, 25, 31],
 [5, 6, 10, 13],
 [0, 3, 7, 8, 12]]

smallest_interval(k_arrays)
```




    (3, 5)



This code runs in O(K * N) time where:

K = number of lists, 

and N = total number of elements in all the lists.

The space compexity is O(K), since we are storing a K length array of pointers.

## Solution 2: Min-Heap
We can use a heap to simplify much of the work in the for loop. 

If we used a heap instead of an array of pointers to track the values we are currently looking at, we would be able to find the local minimum in O(1) time. 

However, we still need to know which list the local minimum is from: for this, we can make use of Python's tuple.

&nbsp;

> The min-heap is a heap where the first element is guaranteed to be minimum of all elements in the heap.

Consider a min-heap consisting of tuples holding the following info:
```
( value,  which list it is from,  index of the value in that list )
```

We can adapt the algorithm to use the heap as follows:

1. Initialize the heap of size K, with all the tuples being: (first value of list, the list it is from,  index 0). 
2. Initialize variables to track the right and left boundaries of the interval
3. Initialize the `local_max` variable to be the max of the first set of values. Since we are using a min-heap, there is no easy way to retrieve the maximum value, so we will need to track it.
4. Pop an element from the top of the heap. The element contains the `local_min`, the list it is from, and index within that list.
5. Compare the new range `(local maximum - local minimum)` and update the current tracked interval if necessary.
6. Increment the `local min`s index, and read the value.
7. If the value is larger than the `local_max`, update the `local_max`. This sets ut up so that the next iteration has an updated version of `local_max`.
8. Create a heap element using the new value, and insert it into the heap.
9. Repeat steps 4-8 until we've exhaused the list.



```python
import heapq

def smallest_interval(k_arrays):
    
    # initialize heap, 
    # each tuple contains (value, the list it is from, value's index)
    heap = [(row[0], i, 0) for i, row in enumerate(k_arrays)]
    heapq.heapify(heap)
    
    # initialize local maximum and interval
    local_max = max(row[0] for row in k_arrays)
    interval = [float('-inf'), float('inf')]
    
    while heap:
        # pop local minimum from the heap
        local_min, k_list, min_index = heapq.heappop(heap)
        # if the new interval is smaller that tracked interval, update it
        if local_max - local_min < interval[1] - interval[0]:
            interval = [local_min, local_max]
        
        # if we've reached the end of the list, break
        if min_index == len(k_arrays[k_list]) - 1:
            return interval
        
        # increment the min index and recalculate local max
        min_index += 1
        next_val = (k_arrays[k_list][min_index])
        local_max = max(next_val, local_max)
        
        # push new values into heap 
        # (next value, list it is from, the value's index in its list)
        heapq.heappush(heap, (next_val, k_list, min_index))
    
```


```python
smallest_interval(k_arrays)
```




    [3, 5]



Popping and pushing an element from the heap takes O(log(N)) time, where N is the number of elements in the heap. 

Since our heap will be maximum size K, and in the worst case, we'll need to iterate for every value in the lists, our total time complexity is O(N log K), where N is the total amount of elements in the lists. 

Our space complexity is O(K), as we are storing at most one element per list in the array.
