## Problem
Implement a stack that has the following methods:

- push(val), which pushes an element onto the stack
- pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
- max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.


## Solution
We can use a list to implement the stack with append and pop. However getting the max from the list in constant time will be trickier. 

To solve this, we can use a secondary stack that only keeps track of the max values at any given time. It will be in sync with the primary stack, and it will have the exact number of elements as our primary stack at any point in time, but the top of the stack will always contain the maximum value of the stack.

When pushing, we check if the element we are pushing is greater than the max value in the secondary stack (by looking at the top which takes constant time).

If it is greater, we push it to be the new max value, if not, then we maintain the previous value.



```python
class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxes = []
        
    def push(self, val):
        self.stack.append(val)
        if self.maxes:
            self.maxes.append(max(val, self.maxes[-1]))
        else:
            self.maxes.append(val)
    def pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop() if self.stack else None
    
    def max(self):
        return self.maxes[-1]
```


```python
stack = MaxStack()
for i in range(10):
    stack.push(i)
stack.max()
```




    9




```python
stack.pop()
stack.max()
```




    8




```python

```
