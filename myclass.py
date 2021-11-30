import pygame
import numpy as np

class key:
    def __init__(self, octave_num, pitch_num): #pitch_num: 0~13 ==> 14개음 (dummy 포함)
        #self.img = image #출력될 키보드 이미지
        #self.posX = x #건반 x좌표
        #self.posY = y #건반 y좌표
        self.frequency = 16.35 * ((1.059**14)**octave_num) * pitch_num #16.35 == C0 주파수, 1.059 곱하면 반음 위 건반 주파수


    def draw(self, screen, image, x, y):
        # screen.blit(self.img, (self.posX, self.posY))
        screen.blit(image, (x, y))

    def sound_key(self):
        duration = 3
        rate = 44100
        frames = int(duration * rate)
        arr = np.cos(2 * np.pi * self.frequency * np.linspace(0, duration, frames))
        sound = np.asarray([32767 * arr, 32767 * arr]).T.astype(np.int16)
        sound = pygame.sndarray.make_sound(sound.copy())
        sound.play()
        pygame.time.wait(500)
        sound.fadeout(50)
        return sound



class piano:
    def __init__(self, screen):
        self.screen = screen

        #출력 이미지 ==> key객체로 전달되어 출력됨
        self.whiteKey = pygame.image.load("whitekey_resized.png")
        self.blackKey = pygame.image.load("blackkey_resized.png")
        self.whiteKeyPressed = pygame.image.load("whitekey_pressed_resized.png")
        self.blackKeyPressed = pygame.image.load("blackkey_pressed_resized.png")

        # 옥타브 수
        self.octave_num = 7

        #백건 키 리스트
        self.whiteKeys = list()
        for i in range(self.octave_num):
            for j in range(7): #C D E F G A B C 7개음
                self.whiteKeys.append(key(i, 2*j))

        #흑건 키 리스트
        self.blackKeys = list()
        for i in range(self.octave_num):
            for j in range(7):
                self.blackKeys.append(key(i, 2*j+1))

        #전체 키 리스트
        self.allKeys = list()
        for i in range(len(self.whiteKeys)):
            self.allKeys.append(self.whiteKeys[i])
            self.allKeys.append(self.blackKeys[i])


        #연주 가능 옥타브
        self.set_octave1 = 0
        self.set_octave2 = 1

        # 피아노 연주 가능한 키보드 입력
        self.keyboard_white_input1 = "zxcvbnm"
        self.keyboard_black_input1 = "sdfghjk"
        self.keyboard_white_input2 = "qwertyu"
        self.keyboard_black_input2 = "2345678"
        # self.all_possible_key_input = self.keyboard_white_input1 + \
        #                               self.keyboard_black_input1 + \
        #                               self.keyboard_white_input2 + \
        #                               self.keyboard_black_input2


    def draw(self, pressed_keys):
        # 건반 출력
        # 도 레 미 파 솔 라 시
        whiteNotes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        # 도# 레# 파# 솔# 라#, dummy는 미-파, 시-도 반음 사이에 위치하는 없는 건반
        blackNotes = ['Cs', 'Ds', 'dummy', 'Fs', 'Gs', 'As', 'dummy']

        #스크린 크기
        screen_width = 1600
        screen_height = 800
        # 화면 테두리 ~ 피아노 사이 여유 공간
        # 건반 사이즈
        whiteKey_size = self.whiteKey.get_rect().size
        whiteKey_width = whiteKey_size[0]  # 백건 가로
        whiteKey_height = whiteKey_size[1]  # 백건 세로
        marginX = int((screen_width - 7 * whiteKey_width * 7) / 2)
        marginY = int((screen_height - whiteKey_height) / 2)

        for i in range(7):  # 7옥타브 피아노 출력
            for noteIdx in range(len(whiteNotes)):  # 백건 출력
                if i == self.set_octave1:
                    if (pressed_keys[self.keyboard_white_input1[noteIdx]]):
                        drawn_image = self.whiteKeyPressed
                    else:
                        drawn_image = self.whiteKey

                elif i == self.set_octave2:
                    if (pressed_keys[self.keyboard_white_input2[noteIdx]]):
                        drawn_image = self.whiteKeyPressed
                    else:
                        drawn_image = self.whiteKey

                else:
                    drawn_image = self.whiteKey

                self.whiteKeys[7*i+noteIdx].draw(self.screen, drawn_image, x=marginX + (7 * whiteKey_width * i) + whiteKey_width * noteIdx,
                         y=int(marginY * 0.7))


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


                    self.blackKeys[7 * i + noteIdx].draw(self.screen, drawn_image,
                                                         x = (7 * whiteKey_width * i) + (noteIdx + 1) * whiteKey_width
                                                             + int(marginX * 0.5),
                                                         y = marginY * 0.7)

    def sound_piano(self, pressed_keys):
        for k,v in pressed_keys.items():
            if v == True:
                if k in "zsxdcfvgbhnjmk":
                    self.allKeys[14*self.set_octave1 + "zsxdcfvgbhnjmk".index(k)].sound_key()

                elif k in "q2w3e4r5t6y7u8":
                    self.allKeys[14*self.set_octave2 + "q2w3e4r5t6y7u8".index(k)].sound_key()




    # def sound_piano(self, pressed_keys):
    #     whiteNotes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    #     # 도# 레# 파# 솔# 라#, dummy는 미-파, 시-도 반음 사이에 위치하는 없는 건반
    #     blackNotes = ['Cs', 'Ds', 'dummy', 'Fs', 'Gs', 'As', 'dummy']
    #     allNotes = ['C', 'Cs', 'D', 'Ds', 'E', 'dummy', 'F', 'Fs', 'G', 'Gs', 'A', 'As', 'B', 'dummy']
    #
    #
    #     for k,v in pressed_keys.items():
    #         if (v == True):
    #             if(k in self.keyboard_white_input1):
    #                 pass
    #             elif(k in self.keyboard_black_input1):
    #                 pass
    #             elif(k in self.keyboard_white_input2):
    #                 pass
    #             elif(k in self.keyboard_black_input2):
    #
    #
    #     # 건반 출력
    #     # 도 레 미 파 솔 라 시
    #     whiteNotes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    #     # 도# 레# 파# 솔# 라#, dummy는 미-파, 시-도 반음 사이에 위치하는 없는 건반
    #     blackNotes = ['Cs', 'Ds', 'dummy', 'Fs', 'Gs', 'As', 'dummy']
    #     allNotes = ['C', 'Cs', 'D', 'Ds', 'E', 'dummy', 'F', 'Fs', 'G', 'Gs', 'A', 'As', 'B', 'dummy']
    #     screen_width = 1600
    #     screen_height = 800
    #     # 화면 테두리 - 피아노 사이 여유 공간
    #     # 건반 사이즈
    #     whiteKey_size = self.whiteKey.get_rect().size
    #     whiteKey_width = whiteKey_size[0]  # 백건 가로
    #     whiteKey_height = whiteKey_size[1]  # 백건 세로
    #     blackKey_size = self.blackKey.get_rect().size
    #     blackKey_width = blackKey_size[0]  # 흑건 가로
    #     blackKey_height = blackKey_size[1]  # 흑건 세로
    #     marginX = int((screen_width - 7 * whiteKey_width * 7) / 2)
    #     marginY = int((screen_height - whiteKey_height) / 2)
    #
    #     for i in range(7):  # 7옥타브 피아노 출력
    #         for noteIdx in range(len(whiteNotes)):  # 백건 출력
    #             if i == self.set_octave1:
    #                 if (pressed_keys[self.keyboard_white_input1[noteIdx]]):
    #                     drawn_image = self.whiteKeyPressed
    #                 else:
    #                     drawn_image = self.whiteKey
    #
    #             elif i == self.set_octave2:
    #                 if (pressed_keys[self.keyboard_white_input2[noteIdx]]):
    #                     drawn_image = self.whiteKeyPressed
    #                 else:
    #                     drawn_image = self.whiteKey
    #
    #             else:
    #                 drawn_image = self.whiteKey
    #
    #             pitchNum = allNotes.index(whiteNotes[noteIdx])
    #             k = key(drawn_image, x=marginX + (7 * whiteKey_width * i) + whiteKey_width * noteIdx,
    #                     y=int(marginY * 0.7), octave_num= i, pitch_num=pitchNum )
    #             k.draw(self.screen)
    #
    #         for noteIdx in range(len(blackNotes)):  # 흑건 출력
    #             if (blackNotes[noteIdx] != 'dummy'):
    #                 if i == self.set_octave1:
    #                     if (pressed_keys[self.keyboard_black_input1[noteIdx]]):
    #                         drawn_image = self.blackKeyPressed
    #                     else:
    #                         drawn_image = self.blackKey
    #
    #                 elif i == self.set_octave2:
    #                     if (pressed_keys[self.keyboard_black_input2[noteIdx]]):
    #                         drawn_image = self.blackKeyPressed
    #                     else:
    #                         drawn_image = self.blackKey
    #
    #                 else:
    #                     drawn_image = self.blackKey
    #
    #                 pitchNum = allNotes.index(blackNotes[noteIdx])
    #                 k = key(drawn_image,
    #                         x=(7 * whiteKey_width * i)
    #                           + (noteIdx + 1) * whiteKey_width
    #                           + int(marginX * 0.5),
    #
    #                         y=marginY * 0.7, octave_num= i, pitch_num=pitchNum )
    #                 k.draw(self.screen)
    #

    #(F1 or F2) + (키패드 숫자) 입력으로 키보드 셋팅 변경
    def set_key1_to_octave(self, keypad_input):
        self.set_octave1 = keypad_input - 1

    def set_key2_to_octave(self, keypad_input):
        self.set_octave2 = keypad_input - 1

