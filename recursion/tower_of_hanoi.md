### Problem
You have 3 rods and N disks. The rods are placed on the first(source) rod. The disks are ordered by size, the smallest disk being at the top.

The goal of the puzzle is to move all disks from the first rod to the last rod using the following rules:
- You can only move one disk at a time
- You cannot place a large disk on top of a smaller disk
- A move consiste of moving a disk from one rod to another rod

Write a function that prints all the necessary steps to complete the Tower of Hanoi.

Assume that the rods are numbered: `First rod == 1, Auxiliary rod == 2, Target rod == 3`


## Solution
The idea is to think about the moves recursively.

1. Recursively move **`N - 1`** disks from the source stack(1) to the middle(auxiliary) stack(2).
2. Move the largest disk that remained in the source stack to target stack.
3. Recursively move **`N - 1`** disks from the middle stack to the target stack.


```python
def tower_of_hanoi(n, a="1", b="2", c="3"):
    if n >= 1:
        tower_of_hanoi(n - 1, a, c, b)
        print(f"Moving {a} to {c}")
        tower_of_hanoi(n - 1, b, a, c)
```


```python
tower_of_hanoi(3, 1, 2, 3)
```

    Moving 1 to 3
    Moving 1 to 2
    Moving 3 to 2
    Moving 1 to 3
    Moving 2 to 1
    Moving 2 to 3
    Moving 1 to 3



```python
tower_of_hanoi(5, a=1, b=2, c=3)
```

    Moving 1 to 3
    Moving 1 to 2
    Moving 3 to 2
    Moving 1 to 3
    Moving 2 to 1
    Moving 2 to 3
    Moving 1 to 3
    Moving 1 to 2
    Moving 3 to 2
    Moving 3 to 1
    Moving 2 to 1
    Moving 3 to 2
    Moving 1 to 3
    Moving 1 to 2
    Moving 3 to 2
    Moving 1 to 3
    Moving 2 to 1
    Moving 2 to 3
    Moving 1 to 3
    Moving 2 to 1
    Moving 3 to 2
    Moving 3 to 1
    Moving 2 to 1
    Moving 2 to 3
    Moving 1 to 3
    Moving 1 to 2
    Moving 3 to 2
    Moving 1 to 3
    Moving 2 to 1
    Moving 2 to 3
    Moving 1 to 3



```python

```
