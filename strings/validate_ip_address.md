### Problem
Write a function to validate an IPv4 Address. 

An IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 

For example input `172.16.254.1` returns True, and `127...1` is invalid as well as `027.0.0.01` 


```python
def valid_part(part):
    n = len(part)
    if n > 3:
        return False
    if part != '' and part[0] == 0 and n > 1:
        return False
    for c in part:
        if c < "0" or c > "9":
            return False
    try:
        num = int(part)
        return num >= 0 and num <= 255
    except Exception as e:
        return False
    
def validate_ip(ip) -> bool:
    count = 0
    for i in ip:
        if i == '.':
            count += 1
    if count != 3:
        return False
    # check for parts
    parts = ip.split(".")
    if len(parts) != 4:
        return False

    for part in parts:
        if not valid_part(part):
            return False
    return True
```


```python
validate_ip("127.0.0.1")
```




    True




```python
validate_ip("1222.22.5.1")
```




    False




```python
validate_ip("1...1")
```




    False




```python

```
