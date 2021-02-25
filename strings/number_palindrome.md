### Convert Number to palindrome
Given an integer, write a function that returns True if the number can be converted into a palindrome, otherwise return False. 

If the conversion steps result in a number bigger than 1 million, return False.


```python
def convertToPalindrome(num):
    if isPalindrome(num):
        return True
    
    while num < 1000000:
        reverted = revert(num)
        num = num + reverted
        if isPalindrome(num):
            return True, num
    return False

def revert(num):
    """O(log10 (n) time -- since we are dividing by 10 every time. | O(1) space"""
    reverted = 0
    while num > 0:
        reverted = (reverted * 10 + num % 10)
        num //= 10
    return reverted

def isPalindrome(x):
    if (x % 10 == 0 and x != 0) or x < 0:
        return False
    reverted = revert(x)
    return x == reverted or x == reverted // 10
```


```python
convertToPalindrome(3335)
```




    (True, 8668)




```python
convertToPalindrome(95999)
```




    False


