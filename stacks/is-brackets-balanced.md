## Problem
Given a string of round, curly and square opening and closing brackets, return whether the brackets are balanced.

For example, 
-  Given the string "([])[]({})", return true.
-  Given the string "([)]" or "(()" return false.



## Solution
If we had only round brackets, one approach is to have a counter and increment it for every opening bracket we see and decrement it on every closing bracket. If we get to the end of string and have a non-zero count, then it means it's unbalanced.

-Ve number would mean more closing brackets,
+Ve number would show the opposite.

In the case of round, curly and square brackets, we must keep track of what kind of brackets they are as well, because we cannot match a square bracket with a curly one.

- We'll use a stack to keep track of the actual bracket character and push onto it whenever we encounter an open bracket, and pop if we encounter a matching closing bracket to the top of the stack.
- If stack == empty or it's not the correct matching bracket, return false.
- If after iterating through the string, we have some left over bracket in the stack, then it means it's unbalanced, so we return whether it's empty or not.



```python
def is_balanced(s):
    stack = []
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            
            if (char == ")" and stack[-1] != "(") or \
               (char == "]" and stack[-1] != "[") or \
               (char == "{" and stack[-1] != "{"):
                return False
            stack.pop()
    
    return len(stack) == 0
```


```python
is_balanced("([])")
```




    True




```python
is_balanced("{{{]}}}")
```




    False




```python
is_balanced("([)]")
```




    False




```python
is_balanced("()()")
```




    True




```python

```
