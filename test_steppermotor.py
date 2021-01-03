from steppermotor_01 import  forward_step_distance1
from steppermotor_01 import  reverse_step_distance1


from time import sleep
import time
step_distance=50
delay = 1

for rotation in (0,4):
    print("rotation no is ",rotation)
    
    print('motor is forward')
    forward_step_distance1(step_distance)
   

    print('motor is stopped')
    sleep(delay)

    print('motor is reverse')
    reverse_step_distance1(step_distance)
    print(' reverse complete')
    
    sleep(delay)
     

