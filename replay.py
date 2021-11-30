import pygame as pg
import numpy as np
import multiprocessing as mp

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((1280, 720))

def sound_piano(freq, duration=3, rate=44100):
    frames = int(duration * rate)
    arr = np.cos(2 * np.pi * freq * np.linspace(0, duration, frames))
    sound = np.asarray([32767*arr, 32767*arr]).T.astype(np.int16)
    sound = pg.sndarray.make_sound(sound.copy())

    return sound

piano_keys = "C C# D D# E F F# G G# A A# B" #매칭될 키

pkey_list = piano_keys.split(' ')

print(pkey_list)

keys ={}
freq = 130.81 #C3의 주파수a

for i in range(3, 7):
    for j in pkey_list:
        keys[j + str(i)] = [sound_piano(freq), freq]
        freq = freq * 1.059

with open("t1.txt", "r") as file:
    keypresses = [eval(line.rstrip()) for line in file]
file.close()
class soundeff:

    def __init__(self):
        self.time = 0



def sound(a, i, time):
    a[i][0].play(0,time,0)
    a[i][0].fadeout(100)


multi =0
p = []


while 1:
    for i in range(len(keypresses)-1):
        key = keypresses[i][1]
        if keypresses[i][0]:
            print(keypresses[i][2])
            j = i + 1
            while 1:
                if keypresses[j][1] == keypresses[i][1]:
                    time = keypresses[j][2] - keypresses[i][2]
                    print("time : ", time)
                    break
                else: j = j + 1

            while 1:
                if pg.time.get_ticks() == keypresses[i][2]:
                    print('tick')
                    p.append(sound_piano(keys[key][1]))
                    p[multi].play(0,time,0)
                    multi += multi
                    print(p)
                    break
        else:
            print(keypresses[i][2], ":0")
            #pg.time.wait(keypresses[i+1][2] - keypresses[i][2])
    break


pg.mixer.quit()
pg.quit()