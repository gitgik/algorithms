### Rocket lauch
Simulate a rocket launch with a countdown (9, 8, 7, ...) in seconds.


```python
import time

def countdown(value):
    if value > 0:
        print(value, end=" ")
        time.sleep(1)
    if value == 0:
        print("\nLift off....!!")
        return
    countdown(value - 1)
```


```python
countdown(10)
```

    10 9 8 7 6 5 4 3 2 1 
    Lift off....!!



```python

```
