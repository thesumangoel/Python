# water - water.mp3 - drank - 35 min
# eyes 30 min - eydone
# pyhsical activity 45 min - exdone

from datetime import datetime
from pygame import mixer
from time import time

def music(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
        else:
            print("invalid input")     

def log(msg):
    with open ('log.txt', 'a') as f:
        f.write(f"{msg} {datetime.now()} \n")



if __name__ == '__main__' :
    time_water = time()
    time_eyes = time()
    time_exer = time()
    watersec = 5
    eyesec = 15
    exersec = 25
    while True:
        if time() - time_water > watersec:
            print("water reminder, please enter 'drank' to stop ")
            music('water.mp3', 'drank')
            time_water = time()
            log('drank water at')
    
    
        if time() - time_eyes > watersec:
            print("eyes exercise reminder, please enter 'eydone' to stop ")
            music('Eyes.mp3', 'eydone')
            time_eyes = time()
            log('eyes exercise done at')       

        if time() - time_exer > watersec:
            print("exercise reminder, please enter 'exdone' to stop ")
            music('Exercise.mp3', 'exdone')
            time_exer = time()
            log('exercise done at') 
    



