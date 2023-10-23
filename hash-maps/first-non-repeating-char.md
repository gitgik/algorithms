## First non-repeating character
Given a string `s` consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

For example, `given s = "abacabad"`, the output should be `c`


```python
# s = asfadsdvsa"

def solution(s):
    count = {}
    for c in s:
        count[c] = 1 + count.get(c, 0)
    
    for c in count:
        if count[c] == 1:
            return c
    return '_'
    
```


```python
solution("abacabad")
```




    'c'




```python
solution("abacabaaacaba")
```




    '_'




```python

```
