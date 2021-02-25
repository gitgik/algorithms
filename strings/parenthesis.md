## Count invalid parenthesis

Given a string of parentheses, write a function to find the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.

### Approach
For each opening parenthesis to be considered valid, they should eventually be matched with an closing parenthesis. If not, they are counted as invalid.
Whenever we encounter an unmatched closing parenthesis, we count as invalid. Eventually, we'll add the unmatched open count to the invalid one.


```python
def count_invalid_parenthesis(string) -> int:
    invalid = 0
    opened = 0
    
    for char in string:
        if char == "(":
            opened += 1
        elif char == ")":
            if opened > 0:
                opened -= 1
            else:
                invalid += 1
    return invalid + opened
```


```python
count_invalid_parenthesis("((()(())")
```




    2




```python
count_invalid_parenthesis("()()()")
```




    0



This solution runs at O(N) time, where N = number of characters in the string.


```python

```
