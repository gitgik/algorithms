```python
"""
Reverse the words in a string but maintain the relative order of delimiters.

For example:
    input = "hello:world/here"
    output = "here:world/hello"

"""
import re


def reverse(string, delimiters):
    """Split the words and delimiters into their respective lists.
    Then reverse the list of words and merge the two lists together.

    Complexity: O(n) time | O(n) space, where n == length of input string.
    """
    words = re.split(f"[{delimiters}]+", string)
    not_words = re.split(f"[^({delimiters})]+", string)

    # remove last empty string if present
    if words[-1] == '':
        words = words[:-1]

    # NOTE: we can in built reverse but there's always another way
    # reversed_strings = list(reversed(words))
    start = 0
    end = len(words) - 1
    while start < end:
        words[start], words[end] = words[end], words[start]
        start += 1
        end -= 1

    output = []
    for index, delimiter in enumerate(not_words):
        print(index)
        output.append(delimiter)
        try:
            print(f"adding {words[index]}")
            output.append(words[index])
        except IndexError:
            pass

    return ''.join(output)
```


```python
reverse("hello:world/here", ":/")
```

    0
    adding here
    1
    adding world
    2
    adding hello
    3





    'here:world/hello'




```python

```
