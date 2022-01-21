## Reconstruct array sequence using clues
The sequence `[0, 1, ..., N]` is jumbled, and the only clue you have for its order is an array showing whether each number is larger or smaller than the last. 

Reconstuct an array that's consistent with this information.

Example:
    Given `[None, +, -, +, +]`, return an array that obeys this order, like: `[1, 2, 0, 3, 4]`

## Solution
Notice that if the clue array contains only consecutive +ves, we can return original sequence of `[0, 1,..,N]`. Similarly, if it contains only consecutive -ves, we return the sequence reversed (to produce decreasing run of numbers).
For example, given `[None, +, -, -, -]` we reverse the last 3 entries of `[0, 1, 2, 3, 4]` to become `[0, 1, 4, 3, 2]`

We can use this little trick to more complicated inputs. We can use a stack to keep track of numbers to be reversed.

As we traverse the clues input array, we keep track of the corresponding elements of the original sequence. 
- For consecutive positive signs, keep the elements of the original sequence.
- For consecutive negative signs, push those elements onto stack. When we come to the end of negatives run, pop elements off one by one to get a decreasing subsequence in our answer. 

Additionally, since there are fewer + or - sign than elements in our answer, we will add the last element to the stack.
We finally empty the stack one by one, appending to our answer.


```python
def reconstruct(array):
    answer = []
    n = len(array) - 1
    stack = []
    
    for i in range(n):
        print(f"iteration {i}")
        if array[i + 1] == "-":
            stack.append(i)
            print(f"answer has {answer}")
        else:
            answer.append(i)
            while stack:
                answer.append(stack.pop())
            
            print(f"answer has {answer}")

    # append last element
    stack.append(n)
    
    # add consecutive -ves run if any, or just the last element
    while stack:
        answer.append(stack.pop())
        
    return answer    
```


```python
reconstruct([None, '+', '-', '-', '-', '+'])
```

    iteration 0
    answer has [0]
    iteration 1
    answer has [0]
    iteration 2
    answer has [0]
    iteration 3
    answer has [0]
    iteration 4
    answer has [0, 4, 3, 2, 1]





    [0, 4, 3, 2, 1, 5]




```python

```
