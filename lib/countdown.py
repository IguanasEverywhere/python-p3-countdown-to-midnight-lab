# your code goes here!
import time

def countdown(n):
    while n > 0:
        print(f'{n} SECOND(S)!')
        n -= 1

    print('HAPPY NEW YEAR!')

def countdown_with_sleep(x):
    while x > 0:
        print(f'{x} SECOND(S)!')
        x -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')