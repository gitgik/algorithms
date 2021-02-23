## Count number of ways to decode.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

### Solution
Let's at some cases to build our approach:


- "", the empty string and our base case, should return 1.
- "1" should return 1, since we can parse it as "a" + "".
- "11" should return 2, since we can parse it as "a" + "a" + "" and "k" + "".
- "111" should return 3, since we can parse it as:
    - "a" + "k" + ""
    - "k" + "a" + ""
    - "a" + "a" + "a" + "".
- "011" should return 0, since no letter starts with 0 in our mapping.
- "705" should also return 0 since no letter starts with 0 just as the example above.

We can use dynamic programming to cache computed steps for a string with one letter, two letters, three, all the way to the end of the string.

Our cache can contain zeros first. 

- Starting from the first digit, to decode it, there's only one way, since a single digit maps directly (only once) to its respective letter. Therefore, `cache[0] = 1.` 
- We build up the cache by incrementing the previously saved total by 1 if and only if the sliced current number falls under 26, inclusive.

Eventually after traversing the string, we'll return the last element in our cache list, since it contains the total number of ways to decode the string.


```python
def num_decodings(s) -> int:
    cache = [0 for i in range(len(s))]
    for i in range(len(s)):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == 0:
            cache[i] = 1
        else:
            num = int(s[i-1:i+1])
            if num <= 26:
                cache[i] = cache[i - 1] + 1
            else:
                cache[i] = cache[i - 1]
    return cache[-1]
```


```python
num_decodings("111")
```




    3




```python
num_decodings("1011")  # (10, 11) and # (10, 1, 1) so 2 ways.
```




    2


