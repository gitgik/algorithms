### Problem

Write a function, `throw_dice(N, faces, total)`, that determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should return 15.

### Approach
For one dice, there are only two posibilities:
1. If the total is less than the faces in the dice, then there's **`1 way`** to get the total.
2. If the total is greater than the faces, it's impossible, so there's **0** ways

For two or more die, we find all the possible outcomes for rolling one dice first. 

THEN, for every new dice, we calculate all the ways it could add to the total, by adding each of its faces to the cumulative total of the previous dice.

We can implement this recursively in O(M^N) time.


```python
def throw_dice_recursively(n, faces, total):
    if n == 1:
        return 1 if total <= faces else 0
    
    ways = 0
    for face in range(1, min(total, faces + 1)):
        ways += throw_dice_recursively(n - 1, faces, total - face)
    
    return ways
```


```python
throw_dice_recursively(3, 6, 7)
```




    15



### Dynamic Programming Approach

We can optimize our previous solution by using dynamic programming.

We create a 2-dimensional array to store number of ways that `N dice` can contribute to the given total.

We know the solution for one dice. `No.of ways == 1 if faces is <= total else 0`. We'll update the first row of the matrix to reflect this.

```python
# Given a total of 7,
# Our matrix will look like this:

ways = [
         [0, 1, 1, 1, 1, 1, 1, 0]  # dice 1 (Last 0 in row because we can't get a 7 from a single dice)
         [0 ,0, 0, 0, 0, 0, 0, 0]  # dice 2
         [0 ,0, 0, 0, 0, 0, 0, 0]  # dice 3
         [0 ,0, 0, 0, 0, 0, 0, 0]  # dice N
       ]
We add a single column at the beginning, to cater for a total of zero.
```

We then loop through each row(each representing a single dice), and through each column (representing potential totals), and through each face value, we accumulate the ways to get to the final total by adding a single face value. 

We'll then obtain the total number of ways from the bottom end of the matrix.


```python
def throw_dice(n, faces, total):
    ways = [[0 for _ in range(total + 1)] for _ in range(n)]

    for t in range(1, total + 1):
        ways[0][t] = 1 if t <= faces else 0
     
    for dice in range(1, n):
        for t in range(1, total + 1):
            for face in range(1, min(t, faces + 1)):
                ways[dice][t] += ways[dice - 1][t - face]
                
    return ways[-1][-1]
```


```python
throw_dice(1, 6, 7)
```




    0




```python
throw_dice(n=3, faces=6, total=4)
```




    3



As you can see above, the number of ways to get a total of 4 from 3 dice is 3. 
```
dice-1 | dice-2 | dice-3 | Total
-------------------------------
  2   +     1    +    1   == 4   FIRST WAY
  1   +     2    +    1   == 4   SECOND WAY
  1   +     1    +    2   == 4   THIRD WAY
```
