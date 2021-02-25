## Job Scheduler 

Implement a job scheduler that takes in a function f and an integer N, and calls the function after N milliseconds.


### 1st Approach
There are many ways to do this. A more straightforward solution is to spin off a new thread on each function we want to delay, sleep for N milliseconds, then run the function.



```python
import threading
from time import sleep

class Scheduler:
    def __init__(self):
        pass
    
    def delay(self, func, n):
        def sleep_then_call(n):
            sleep(n / 1000)
            func()
        
        t = threading.Thread(target=sleep_then_call)
        t.start()
```

###  2nd Approach
While this works, there's a huge problem with our logic: we spin off a new thread each time we call delay! The number of threads will easily grow as we have more functions to schedule. 

We can solve this by having one dedicated thread to call functions, and storing functions we need to call in some data structure, say a list. 

Then do polling to check when to run a function. We can store each function along with a unix epoch timestamp that tells when it should run. 

After checking the list for any jobs that are due to run, we run them and remove them from the list.


```python
import threading
from time import sleep, time

class Scheduler:
    def __init__(self):
        self.functions = []  # saves tuple of (function, time-to-run-it)
        t = threading.Thread(target=self.poll)
        t.start()
        
    def poll(self):
        while True:
            now = time() * 1000.  # change from sec to ms
            for function, due in self.functions:
                if now > due:
                    function()
            self.functions = [(function, due) for (function, due) in self.functions if due > now]
            sleep(0.01)
            
    def delay(self, function, n):
        self.functions.append((function, time() * 1000 + n))
```

You can go further by doing:
- Extend the scheduler to allow functions with variables
- Use a heap instead of a list to keep track of the next job to run more efficiently
- Come up with a way to get a due function, say a condition variable instead of polling
- Use a threadpool to run more than one thread without the chance of starvation (when one thread is not able to run because of another running thread) 


```python

```
