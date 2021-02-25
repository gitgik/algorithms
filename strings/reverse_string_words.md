## Problem

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

### Approach 

Since strings are immutable, a mutable string can be represented as a list of characters in a buffer e.g  `['h','e','l','l','o',' ','w','o','r','l','d']` == 'hello world'

First we reverse entire string to get `'dlrow olleh'`, then we reverse each word within the string to obtain original words.


```python
def reverse(string_list: list, start: int, end: int) -> str:
    while start < end:
        string_list[start], string_list[end] = string_list[end], string_list[start]
        start += 1
        end -= 1

def reverse_words(string_list: list) -> str:
    reverse(string_list, 0, len(string_list) - 1)
    start = 0
    for i in range(len(string_list)):
        if string_list[i] == " ":
            reverse(string_list, start, i - 1)
            start = i + 1
    # we need to reverse the last sub-string
    reverse(string_list, start, len(string_list) - 1)
    return "".join(string_list)
```


```python
string_list = list("well hello there")
reverse_words(string_list)
```




    'there hello well'




