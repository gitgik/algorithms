## Implement Regular Expression Matching

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.


```python
### Approach

# helper function that check first matching character

# base case: if r == '', return s == ''  //  s = "123" .. recursive(s, r)
# Otherwise if the first thing in r is not an asterisk(*), then match the first character of both r and s. If they match, return match(r[1:], s[1:]). If they don't return false.
# If the first things in r is an asterisk, then 

def matches_first_char(s, r):
    return s[0] == r[0] or (r[0] == "." and len(s) > 0)

def matches(s, r):
    # base case 
    if r == "":
        return s == ""
    
    # The first char in the regex r is not proceeded by a *
    if len(r) == 1 or r[0] != "*":
        if matches_first_char(s, r):
            return matches(s[1:], r[1:])
        else:
            return False
        
    # The first char in r is proceeded by *
    if matches(s, r[2:]):
        # Try zero length
        return True
    
    # If it doesn't match staight away, try globbing until
    # the first character of the string doesn't match anymore.
    i = 0
    while matches_first_char(s[i:], r):
        if matches(s[i+1:], r[2:]):
            return True
        i += 1
    return False
```


```python
r = "tx."
s = "txt"
matches(s, r)
```




    True



This takes **O(len(s) * len(r))** time and space, since we potentially need to iterate over each suffix substring again for each character.

Fun fact: Stephen Kleene introduced the * operator in regular expressions and as such, it is sometimes referred to as the Kleene star.


```python

```
