# Progresstracker
Progresstracker for ipython notebooks

![demoe-image](/progresstracker_demo.gif)

## Usage:
```python
from time import sleep
from progresstracker import progresstracker

steps_in_loop = 100
prog = progresstracker(steps_in_loop) #init object with number of loops to be executed

for i in range(steps_in_loop):  
    prog.step_print()  #count step and print output
    #progress, current_run_time, expected_time, expected_rest_time = prog.step() #perform step and get times if you want to use your own display function
    sleep(0.1)  #do something
```

Output should look like this:

