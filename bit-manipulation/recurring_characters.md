## Return recurring character in a string 
Given a string, return the first recurring character in it, or null if no recurring character.

Example:
- given string `"acddab"`, return `d`.
- given string `"algorithms"` return null.


### Solution 
We can solve this problem by keeping track of the characters we've seen in a set. Once we encounter it again, we return it.



```python
def recurring_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None
```

This runs in O(N) space and time, since we are iterating over the string.
We can improve the space complexity by using bitwise operators to set the bits of characters already seen.


```python
def first_recurring(s):
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if (checker & (1 << val)) > 0:
            return char
        checker |= (1 << val)
    return None
```


```python
first_recurring("fluffywombat")
```




    'f'


