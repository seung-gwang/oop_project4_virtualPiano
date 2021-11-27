import pygame as pg
import numpy as np

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((1280, 720))

def sound_piano(freq, duration=3, rate=44100):
    frames = int(duration * rate)
    arr = np.cos(2 * np.pi * freq * np.linspace(0, duration, frames))
    sound = np.asarray([32767*arr, 32767*arr]).T.astype(np.int16)
    sound = pg.sndarray.make_sound(sound.copy())

    return sound

keyboard = "a w s e d f t g y h u j" #유저가 누를 키들
piano_keys = "C3 C#3 D3 D#3 E3 F3 F#3 G3 G#3 A3 A#3 B3" #매칭될 키
ukey_list = keyboard.split(' ')
pkey_list = piano_keys.split(' ')
keys = dict.fromkeys(ukey_list)
freq = 130.81 #C3의 주파수a
for i in range(len(ukey_list)):
    keys[ukey_list[i]] = [pkey_list[i], sound_piano(freq)]
    freq = freq * 1.059

recording = 1
keypress = []
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            key = str(event.unicode)
            if key == 'j':
                running = False
            keys[key][1].play()
            if recording == 1:
                keypress.append([1, keys[key][0], pg.time.get_ticks()]) # 음 누를때 기록
        if event.type == pg.KEYUP:
            key = str(event.unicode)
            keys[key][1].fadeout(30)
            if recording == 1:
                keypress.append([0, keys[key][0], pg.time.get_ticks()]) # 쉬는 박자 기록

print(keypress)


with open("t1.txt", "w") as file:
    for i in range(len(keypress)):
        file.write(str(keypress[i]) + '\n')
file.close()

pg.mixer.quit()
pg.quit()