## Problem
Write a min max stack class. The class should support pushing, 
popping values on and off the stack, peeking values at the top of the stack, and getting the minimum and maximum values from the stack.
All operations should run on constant time and constant space.


```python
# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.min_max_stack = []
        self.stack = []
        
    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.min_max_stack.pop()
        return self.stack.pop()

    def push(self, number):
        new_min_max = {'max': number, 'min': number}
        if len(self.min_max_stack):
            current_min_max = self.min_max_stack[len(self.min_max_stack) - 1]
            new_min_max['max'] = max(number, current_min_max['max'])
            new_min_max['min'] = min(number, current_min_max['min'])
        self.min_max_stack.append(new_min_max)
        self.stack.append(number)

    def get_min(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]['min']

    def get_max(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]['max']
```


```python
# test it out
import unittest

def test_min_max_peek(self, min, max, peek):
    self.assertEqual(self.stack.get_min(), min)
    self.assertEqual(self.stack.get_max(), max)
    self.assertEqual(self.stack.peek(), peek)
        
class Test(unittest.TestCase, MinMaxStack):
    def test_min_max_stack_and_peek(self):
        self.stack = MinMaxStack()
        self.stack.push(3)
        test_min_max_peek(self, 3, 3, 3)
        
    def test_pushing_to_stack(self):
        self.stack = MinMaxStack()
        self.stack.push(1)
        self.assertEqual(self.stack.stack, [1])
    
    def test_popping_from_stack(self):
        self.stack = MinMaxStack()
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(7)
        self.assertEqual(self.stack.pop(), 7)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```
