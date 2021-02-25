## Kaprekar's constant

The number 6174 is known as Kaprekar's contant, after the mathematician who discovered an associated property: for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value. 

The procedure is as follows:

- For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.
- Subtract the smaller number from the larger number.

For example, this algorithm terminates in three steps when starting from 1234:

```js
4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
```
Write a function that returns how many steps this will take for a given input N.

## Solution
To solve this imperatively, we can implement a while loop that continually runs the procedure described above until obtaining the number 6174. 

For each iteration of the loop we will increment a counter for the number of steps, and return this value at the end.

We also use a helper function that prepends zeros if necessary so that the number always remains four digits long, before creating the ascending and descending integers.


```python
def get_digits(n):
    digits = str(n)
    if len(digits) == 4:
        return digits
    else:
        return '0' * (4 - len(digits)) + digits

def count_steps(n):
    count = 0
    while n != 6174:
        n = int(''.join(sorted(get_digits(n), reverse=True))) - int(''.join(sorted(get_digits(n))))
        count += 1
    return count
```


```python
count_steps(12)
```




    3




```python
### Recursive solution
def count_steps(n, steps=0):
    if n == 6174:
        return steps
    num = int(''.join(sorted(get_digits(n), reverse=True))) - int(''.join(sorted(get_digits(n))))
    
    return count_steps(num, steps + 1)
```


```python
count_steps(1234)
```




    3




```python

```
