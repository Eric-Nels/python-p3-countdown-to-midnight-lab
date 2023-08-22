import time 

def countdown(integer):
    while integer > 0:
        print(f'{integer} SECOND(S)!')
        integer -= 1
    while integer == 0:
        print('HAPPY NEW YEAR!')
        integer -= 1

def countdown_with_sleep(integer):
    while integer > 0:
        print(f'{integer} SECOND(S)!')
        integer -= 1
        time.sleep(1)
    while integer == 0:
        print('HAPPY NEW YEAR!')
        integer -= 1    