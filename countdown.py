import time

seconds = input('Enter time in seconds')

def countdown_timer(seconds):
    while seconds>0:
        min=int(seconds/60)
        secs=int(seconds%60)

        timer=f'{min}:{secs}'
        
        print(timer, end='\r')
        time.sleep(1)

        seconds -= 1

    print('time up')

countdown_timer(int(seconds))