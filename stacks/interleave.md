### Problem

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

Sample input:

```python
[1, 2, 3, 4, 5]
```

Sample output:

```python
[1, 5, 2, 4, 3]
```

If the stack is `[1, 2, 3, 4]`, it should become `[1, 4, 2, 3]`.

Try working backwards from the end state.

### Approach

* Given [1, 2, 3, 4, 5] we want [1, 5, 2, 4, 3].
* We can see this is just a pairing of a queue with (5, 4) and a stack of [3, 2, 1] where we first pop off stack and then get from the queue.
* At this point, we can get to the above from a queue of (3, 2, 1, 5, 4)
* [3, 2, 1, 5, 4] is just a rotation of (5, 4, 3, 2, 1)


The steps will look as follows: 

1. Get the elements from the stack and pop them into the queue. (5, 4, 3, 2, 1)
2. Rotate half of the queue by looping through half stack-size / 2 times, getting the elements and putting them back in. (1, 2, 3, 5, 4)
3. Put ceil(len(stack) / 2) elements into the stack. The queue is now (5, 4) and stack is [3, 2, 1]
4. Pair them up len(stack) / 2 times. If stack is still not empty, pop one more time
5. Move all elements from the queue to the stack


```python
import math
from queue import Queue

def interleave(stack):
    stack = [1, 2, 3, 4, 5]
    queue = Queue()
    size = len(stack)

    while stack:
        queue.put(stack.pop())

    for _ in range(size // 2):
        queue.put(queue.get())
        
    for _ in range(math.ceil(size / 2.0)):
        stack.append(queue.get())
    
    for _ in range(size // 2):
        queue.put(stack.pop())
        queue.put(queue.get())
    
    if stack:
        queue.put(stack.pop())
        
    while not queue.empty():
        stack.append(queue.get())
        
    return queue.queue, stack
```


```python
interleave([1, 2, 3, 4, 5])
```




    (deque([]), [1, 5, 2, 4, 3])


