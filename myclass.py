import pygame
import numpy as np

key0 = {16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87}
white0 = {16.35, 18.35, 20.60, 21.83, 24.50, 27.50, 30.87}
black0 = {17.32, 19.45, 0, 23.12, 25.96, 29.14, 0}

def sound_piano(freq, duration=3, rate=44100):
    frames = int(duration * rate)
    arr = np.cos(2 * np.pi * freq * np.linspace(0, duration, frames))
    sound = np.asarray([32767*arr, 32767*arr]).T.astype(np.int16)
    sound = pygame.sndarray.make_sound(sound.copy())

    return sound

class key:

    def __init__(self, image, x, y, f):
        self.img = image #출력될 키보드 이미지
        self.posX = x #건반 x좌표
        self.posY = y #건반 y좌표
        self.freq = f
        self.sound = self.sound_piano()
        # i = 0
        # freq = 16.35
        # while not i == (x-16)/32:
        #     freq = freq*1.05946
        # self.freq = freq

    def make_sound(self): #소리출력
        pass

    def draw(self, screen):
        screen.blit(self.img, (self.posX, self.posY))

    def pressed(self):
        self.img = self.img_pressed

    def sound_piano(self, duration=3, rate=44100):
        frames = int(duration * rate)
        arr = np.cos(2 * np.pi * self.freq * np.linspace(0, duration, frames))
        sound = np.asarray([32767 * arr, 32767 * arr]).T.astype(np.int16)
        sound = pygame.sndarray.make_sound(sound.copy())
        return sound

    def sound(self, time):
        self.sound.play()
        pygame.time.wait(time) #wait는 동시 입력시 죽어버림
        self.sound.fadeout(50)

class piano:
    def __init__(self, screen):
        self.screen = screen

        #출력 이미지 ==> key객체로 전달되어 출력됨
        self.whiteKey = pygame.image.load("whitekey_resized.png")
        self.blackKey = pygame.image.load("blackkey_resized.png")
        self.whiteKeyPressed = pygame.image.load("whitekey_pressed_resized.png")
        self.blackKeyPressed = pygame.image.load("blackkey_pressed_resized.png")

        self.octave_num = 7  # 옥타브 수
        #연주 가능 옥타브
        self.set_octave1 = 0
        self.set_octave2 = 1

        # 피아노 연주 가능한 키보드 입력
        self.keyboard_white_input1 = "zxcvbnm"
        self.keyboard_black_input1 = "sdfghjk"
        self.keyboard_white_input2 = "qwertyu"
        self.keyboard_black_input2 = "2345678"
        self.all_possible_key_input = self.keyboard_white_input1 + \
                                      self.keyboard_black_input1 + \
                                      self.keyboard_white_input2 + \
                                      self.keyboard_black_input2
    def draw(self, pressed_keys):
        # 건반 출력
        # 도 레 미 파 솔 라 시
        whiteNotes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        # 도# 레# 파# 솔# 라#, dummy는 미-파, 시-도 반음 사이에 위치하는 없는 건반
        blackNotes = ['Cs', 'Ds', 'dummy', 'Fs', 'Gs', 'As', 'dummy']
        screen_width = 1600
        screen_height = 800
        # 화면 테두리 - 피아노 사이 여유 공간
        # 건반 사이즈
        whiteKey_size = self.whiteKey.get_rect().size
        whiteKey_width = whiteKey_size[0]  # 백건 가로
        whiteKey_height = whiteKey_size[1]  # 백건 세로
        blackKey_size = self.blackKey.get_rect().size
        blackKey_width = blackKey_size[0]  # 흑건 가로
        blackKey_height = blackKey_size[1]  # 흑건 세로
        marginX = int((screen_width - 7 * whiteKey_width * 7) / 2)
        marginY = int((screen_height - whiteKey_height) / 2)

        for i in range(7):  # 7옥타브 피아노 출력
            for noteIdx in range(len(whiteNotes)):  # 백건 출력
                if i == self.set_octave1:
                    freq = white0[noteIdx]*2^i
                    if (pressed_keys[self.keyboard_white_input1[noteIdx]]):
                        drawn_image = self.whiteKeyPressed
                    else:
                        drawn_image = self.whiteKey

                elif i == self.set_octave2:
                    freq = white0[noteIdx] * 2 ^ i
                    if (pressed_keys[self.keyboard_white_input2[noteIdx]]):
                        drawn_image = self.whiteKeyPressed
                    else:
                        drawn_image = self.whiteKey

                else:
                    drawn_image = self.whiteKey

                k = key(drawn_image, x=marginX + (7 * whiteKey_width * i) + whiteKey_width * noteIdx,
                        y=int(marginY * 0.7), f = freq)
                k.draw(self.screen)
                if(pressed_keys[self.keyboard_white_input1[noteIdx]]):
                    k.soun

            for noteIdx in range(len(blackNotes)):  # 흑건 출력
                if (blackNotes[noteIdx] != 'dummy'):
                    if i == self.set_octave1:
                        if (pressed_keys[self.keyboard_black_input1[noteIdx]]):
                            drawn_image = self.blackKeyPressed
                        else:
                            drawn_image = self.blackKey

                    elif i == self.set_octave2:
                        if (pressed_keys[self.keyboard_black_input2[noteIdx]]):
                            drawn_image = self.blackKeyPressed
                        else:
                            drawn_image = self.blackKey

                    else:
                        drawn_image = self.blackKey

                    k = key(drawn_image,
                            x=(7 * whiteKey_width * i)
                              + (noteIdx + 1) * whiteKey_width
                              + int(marginX * 0.5),

                            y=marginY * 0.7)
                    k.draw(self.screen)

    #(F1 or F2) + (키패드 숫자) 입력으로 키보드 셋팅 변경
    def set_key1_to_octave(self, keypad_input):
        self.set_octave1 = keypad_input - 1

    def set_key2_to_octave(self, keypad_input):
        self.set_octave2 = keypad_input - 1

