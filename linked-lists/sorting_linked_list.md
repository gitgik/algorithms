
## Problem
Given a linked list, sort it in **O(n log N)** time and **constant** space.
For example: the linked list 4 -> 1 -> -3 -> 99 should become
-3 -> 1 -> 4 -> 99

## Solution
We can sort a linked list in O(n log n) by doing something like merge sort:

- Split the list by half using fast and slow pointers
- Recursively sort each half list (base case: when size of list is 1)
- Merge the sorted halves together by using the standard merge algorithm

However, since we are dividing the list in half and recursively sorting it, the function call stack will grow and use up to log n space. We want to do it in constant O(1) space.

Since the problem comes from the call stack (built by recursion), we can transform the algorithm into an iterative one and keep track of the array indices ourselves to use only constant space.
We can do this by merging blocks at a time from the bottom-up. 

Let k be equal to 1. Then  we'll merge lists of size k into list of size 2k.

Then double k and repeat, until there are no more merges left.

Consider this example: 
```
linked list:
    8 -> 6 -> 3 -> 21 -> 23 -> 5
```

After the first pass, we'll combine all pairs so that they are sorted:
```
(6 -> 8) -> and -> (3 -> 21) -> and -> (5 -> 23)
```
And then all groups of 4 (since we doubled k, so k=2 * 2):
```
(3 -> 6 -> 8 -> 21 ) ->and->   (5 -> 23)
```
And then finally the entire list
```
3 -> 5 -> 6 -> 8 -> 21 -> 23 (now sorted!)
```


```python
class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

def sort(head):
    if not head:
        # empty linked list. return
        return head
    
    k = 1
    while True:
        first = head
        head = None
        tail = None
        
        merges = 0
        while first:
            merges += 1
            
            # Move second 'k' steps forward.
            second = first
            first_size = 0
            for i in range(k):
                first_size += 1
                second = second.next
                if second is None:
                    # list contains only one node. break.
                    break
            
            # Merge lists "first" and "second"
            second_size = k
            while first_size > 0 or (second_size > 0 and second is not None):
                temp = None
                
                if first_size == 0:
                    temp = second
                    second = second.next
                    second_size -= 1
                elif second_size == 0 or second is None:
                    temp = first
                    first = first.next
                    first_size -= 1
                elif first.value <= second.value:
                    temp = first
                    first = first.next
                    first_size -= 1
                else:
                    temp = second
                    second = second.next
                    second_size -= 1

                if tail is not None:
                    tail.next = temp
                else:
                    head = temp
                tail = temp
            
            first = second
            
        tail.next = None
        if merges <= 1:
            return head
        
        k = k * 2
```


```python
# test with linked list: 8 -> 6 -> 3 -> 21 -> 12 -> 20 -> 5
linked_list = Node(8, nxt=Node(6, nxt=Node(3, nxt=Node(21, nxt=Node(12, nxt=Node(20, nxt=Node(5)))))))
sorted_list = sort(linked_list)

# traverse the linked list
def traverse(head):
    current = head
    li = []
    while current:
        li.append(current.value)
        current = current.next
    return li

traverse(sorted_list)
```




    [3, 5, 6, 8, 12, 20, 21]




```python

```


```python

```
