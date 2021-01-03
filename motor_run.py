from steppermotor_01 import  forward_step_distance1,reverse_step_distance1
from steppermotor_02 import  forward_step_distance2,reverse_step_distance2
from steppermotor_03 import  forward_step_distance3,reverse_step_distance3
from steppermotor_04 import  forward_step_distance4,reverse_step_distance4
from steppermotor_05 import  forward_step_distance5,reverse_step_distance5
from steppermotor_06 import  forward_step_distance6,reverse_step_distance6
from steppermotor_07 import  forward_step_distance7,reverse_step_distance7
from steppermotor_08 import  forward_step_distance8,reverse_step_distance8

from time import sleep
import RPi.GPIO as GPIO

import threading
delay=1


for x in range(0,10):
    
    forward_step_distance2(5)
    reverse_step_distance2(5)
#   forward_step_distance2(3)
    


"""for x in range(0,3):
    
    
    
    forward_step_distance1(50)
    reverse_step_distance1(50)

    sleep(delay)
    
    forward_step_distance2(50)
    reverse_step_distance2(50)
    
    sleep(delay)


    forward_step_distance3(50)
    reverse_step_distance3(50)
    
    sleep(delay)

    
    forward_step_distance4(50)
    reverse_step_distance4(50)
    
    sleep(delay)
    
    forward_step_distance5(50)
    reverse_step_distance5(50)
    
    sleep(delay)
    
    forward_step_distance6(50)
    reverse_step_distance6(50)
    
    sleep(delay)
    
    forward_step_distance7(50)
    reverse_step_distance7(50)
    
    sleep(delay)
    
    forward_step_distance8(50)
    reverse_step_distance8(50)
    
    sleep(delay)
    GPIO.cleanup()"""


def motor1():
    forward_step_distance1(3)
    reverse_step_distance1(3)
    
def motor2():
    forward_step_distance2(4)
    reverse_step_distance2(4)
 
'''def motor3():
    forward_step_distance3(50)
    reverse_step_distance3(50)
    
def motor4():
    forward_step_distance4(50)
    reverse_step_distance4(50)

def motor5():
    forward_step_distance5(50)
    reverse_step_distance5(50)
    
def motor6():
    forward_step_distance6(50)
    reverse_step_distance6(50)
    
def motor7():
    forward_step_distance7(50)
    reverse_step_distance7(50)
    
def motor8():
    forward_step_distance8(50)
    reverse_step_distance8(50)
    '''
#threads have been defined
if __name__=="__main__":
    
    '''a=threading.Thread(target=motor1,args=())
    b=threading.Thread(target=motor2,args=())'''
    '''c=threading.Thread(target=motor3,args=())
    d=threading.Thread(target=motor4,args=())
    e=threading.Thread(target=motor5,args=())
    f=threading.Thread(target=motor6,args=())
    g=threading.Thread(target=motor7,args=())
    h=threading.Thread(target=motor8,args=())
    '''
    #to initiate threads
    '''a.start()
    b.start()'''
    '''c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    '''
    

"""forward_step_distance2(100)
forward_step_distance3(100)
forward_step_distance4(100)
forward_step_distance5(100)
forward_step_distance6(100)
forward_step_distance7(100)
forward_step_distance8(100)


reverse_step_distance2(100)
reverse_step_distance3(100)
reverse_step_distance4(100)
reverse_step_distance5(100)
reverse_step_distance6(100)
reverse_step_distance7(100)
reverse_step_distance8(100)





from time import sleep
import time
step_distance=300
delay = 1

for rotation in (0,3):
    print("rotation no is ",rotation)
    
    print('motor is forward')
    forward_step_distance(step_distance)
    

    print('motor is stopped')
    sleep(delay)

    print('motor is reverse')
    reverse_step_distance(step_distance)
    print(' reverse complete')
    
    sleep(delay)
     



"""
