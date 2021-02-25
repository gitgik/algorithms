## Hit Counter

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

- record(timestamp): records a hit that happened at timestamp
- total(): returns the total number of hits recorded
- range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

What if our system has limited memory?


```python
class HitCounter:
    def __init__(self):
        self.hits = []
    
    def record(timestamp):
        self.hits.append(timestamp)
    
    def total():
        return len(self.hits)
    
    def range(lower, upper):
        count = 0
        for hit in self.hits:
            if lower <= hit <= upper:
                count += 1
        return count
```

Here record and count are constant time operations. Range takes O(N) time.

One tradeoff we can make is to use a sorted list or BST to keep track of the hits. This allows range operation to take O(log N) time. We can use Python's [bisect](https://docs.python.org/3/library/bisect.html) to handle sortedness.



```python
import bisect


class HitCounter:
    def __init__(self):
        self.hits = []
        
    def record(timestamp):
        bisect.insort_left(self.hits, timestamp)
    
    def total():
        return len(self.hits)
    
    def range(lower, upper):
        low = bisect.bisect_left(self.hits, lower)
        high = bisect.bisect_right(self.hits, upper)
        return high - low
```

While this is time efficient, it'll still take a lot of space because we are still saving each timestamp into the list.

We can sacrifice accuracy for memory by grouping timestamps into minutes or hours. We'll lose accuracy around the boarders but use upto a constant factor less space.  

For our solution, we'll keep track of each group in a tuple, where the first item is a timestamp (in minutes) and the second item is the number of hits occuring within that minute. We'll sort the tuple by minute to allow record to run in O(log N) time.

```
tuple = (minute,  hits_within_this_minute)
```


```python
import bisect
from math import floor

class HitCounter:
    def __init__(self):
        self.hits = []
        self.counter = 0
        
    def record(timestamp):
        self.counter += 1
        
        minute = floor(timestamp / 60)
        
        idx = bisect.bisect_left([hit[0] for hit in self.hits], minute)
        
        if idx < len(hits) and self.hits[idx][0] == minute:
            self.hits[idx] = (minute, self.hits[idx][1] + 1)
        else:
            self.hits.insert(idx, (minute, 1))
        
    def total():
        return self.counter
    
    def range(lower, higher):
        lo = floor(lower / 60)
        hi = floor(higher / 60)
        lo_idx = bisect.bisect_left([hit[0] for hit in self.hits], lo)
        hi_idx = bisect.bisect_right([hit[0] for hit in self.hits], hi)
        
        # sum the counts of each tuple within the range(lo, hi)
        return sum(self.hits[i][0] for i in range(lo_idx, hi_idx))
```


```python

```
