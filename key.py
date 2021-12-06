import numpy as np
import pygame

class key:
    def __init__(self, octave_num, pitch_num): #pitch_num: 0~13 ==> 14개음 (dummy 포함)

        self.__stack = []
        if pitch_num > 5:
            self.__frequency = 130.81 * ((2)**octave_num) * 1.059 ** (pitch_num-1) #16.35 == C0 주파수, 1.059 곱하면 반음 위 건반 주파수
        elif (pitch_num == 5 or pitch_num == 13):
            self.__frequency = 0
        else :
            self.__frequency = 130.81 * ((2) ** octave_num) * 1.059 ** (pitch_num)

    def draw(self, screen, image, x, y):
        screen.blit(image, (x, y))

    def sound_key(self, v):
        if self.__frequency != 0:
            if v == False:
                tempsound = self.__stack.pop()
                tempsound.fadeout(100)
            else:
                duration = 3
                rate = 44100
                frames = int(duration * rate)
                arr = np.cos(2 * np.pi * self.__frequency * np.linspace(0, duration, frames))
                sound = np.asarray([32767 * arr, 32767 * arr]).T.astype(np.int16)
                sound = pygame.sndarray.make_sound(sound.copy())
                sound.set_volume(0.3)
                self.__stack.append(sound)
                sound.play()