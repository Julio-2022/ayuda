import time
def tempo(seconds):
    while seconds > 0:
        mins = int (seconds/60)
        seg = int (seconds%60)
        timer = f'{mins}:{seg}'
        print(timer)
        seconds -= 1
    print("se acabo el tiempo")
seconds = input ("escribe el tiempo en ")
tempo(int(seconds))