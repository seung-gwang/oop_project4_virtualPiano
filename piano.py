from key import *
import pygame

class piano:
    def __init__(self, screen):
        self.__screen = screen

        #출력 이미지 ==> key객체로 전달되어 출력됨
        self.__whiteKey = pygame.image.load("whitekey_resized.png")
        self.__blackKey = pygame.image.load("blackkey_resized.png")
        self.__whiteKeyPressed = pygame.image.load("whitekey_pressed_resized.png")
        self.__blackKeyPressed = pygame.image.load("blackkey_pressed_resized.png")

        # 옥타브 수
        self.__octave_num = 7

        #백건 키 리스트
        self.__whiteKeys = list()
        for i in range(self.__octave_num):
            for j in range(7): #C D E F G A B C 7개음
                self.__whiteKeys.append(key(i, 2*j))

        #흑건 키 리스트
        self.__blackKeys = list()
        for i in range(self.__octave_num):
            for j in range(7):
                self.__blackKeys.append(key(i, 2*j+1))

        #전체 키 리스트
        self.__allKeys = list()
        for i in range(len(self.__whiteKeys)):
            self.__allKeys.append(self.__whiteKeys[i])
            self.__allKeys.append(self.__blackKeys[i])


        #연주 가능 옥타브
        self.__set_octave1 = 0
        self.__set_octave2 = 1

        # 피아노 연주 가능한 키보드 입력
        self.__keyboard_white_input1 = "zxcvbnm"
        self.__keyboard_black_input1 = "sdfghjk"
        self.__keyboard_white_input2 = "qwertyu"
        self.__keyboard_black_input2 = "2345678"
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
        whiteKey_size = self.__whiteKey.get_rect().size
        whiteKey_width = whiteKey_size[0]  # 백건 가로
        whiteKey_height = whiteKey_size[1]  # 백건 세로
        marginX = int((screen_width - 7 * whiteKey_width * 7) / 2)
        marginY = int((screen_height - whiteKey_height) / 2)

        for i in range(7):  # 7옥타브 피아노 출력
            for noteIdx in range(len(whiteNotes)):  # 백건 출력
                if i == self.__set_octave1:
                    if (pressed_keys[self.__keyboard_white_input1[noteIdx]][0]):
                        drawn_image = self.__whiteKeyPressed
                    else:
                        drawn_image = self.__whiteKey

                elif i == self.__set_octave2:
                    if (pressed_keys[self.__keyboard_white_input2[noteIdx]][0]):
                        drawn_image = self.__whiteKeyPressed
                    else:
                        drawn_image = self.__whiteKey

                else:
                    drawn_image = self.__whiteKey

                self.__whiteKeys[7*i+noteIdx].draw(self.__screen, drawn_image, x=marginX + (7 * whiteKey_width * i) + whiteKey_width * noteIdx,
                         y=int(marginY * 0.7))


            for noteIdx in range(len(blackNotes)):  # 흑건 출력
                if (blackNotes[noteIdx] != 'dummy'):
                    if i == self.__set_octave1:
                        if (pressed_keys[self.__keyboard_black_input1[noteIdx]][0]):
                            drawn_image = self.__blackKeyPressed
                        else:
                            drawn_image = self.__blackKey

                    elif i == self.__set_octave2:
                        if (pressed_keys[self.__keyboard_black_input2[noteIdx]][0]):
                            drawn_image = self.__blackKeyPressed
                        else:
                            drawn_image = self.__blackKey

                    else:
                        drawn_image = self.__blackKey


                    self.__blackKeys[7 * i + noteIdx].draw(self.__screen, drawn_image,
                                                         x = (7 * whiteKey_width * i) + (noteIdx + 1) * whiteKey_width
                                                             + int(marginX * 0.5),
                                                         y = marginY * 0.7)

    def sound_piano(self, pressed_keys):
        for k,v in pressed_keys.items():
            if v[0] == True: #키를 눌렀을때
                if v[1] == True:
                    run = True
                    if k in "zsxdcfvgbhnjmk":
                        self.__allKeys[14*self.__set_octave1 + "zsxdcfvgbhnjmk".index(k)].sound_key(run)

                    elif k in "q2w3e4r5t6y7u8":
                        self.__allKeys[14*self.__set_octave2 + "q2w3e4r5t6y7u8".index(k)].sound_key(run)
            elif v[0] == False: #키를 뗐을때
                if v[1] == True:
                    run = False
                    if k in "zsxdcfvgbhnjmk":
                        self.__allKeys[14*self.__set_octave1 + "zsxdcfvgbhnjmk".index(k)].sound_key(run)

                    elif k in "q2w3e4r5t6y7u8":
                        self.__allKeys[14*self.__set_octave2 + "q2w3e4r5t6y7u8".index(k)].sound_key(run)

    def replay(self, running, keypress, click_time):
        keyboard_white_input1 = "zxcvbnm"
        keyboard_black_input1 = "sdfghjk"
        keyboard_white_input2 = "qwertyu"
        keyboard_black_input2 = "2345678"
        all_possible_key_input = keyboard_white_input1 + keyboard_black_input1 + keyboard_white_input2 + keyboard_black_input2
        pressed_keys = dict()
        for char in keyboard_white_input1 + keyboard_white_input2 + keyboard_black_input1 + keyboard_black_input2:
            pressed_keys[char] = [False, False]

        while running:
            self.draw(pressed_keys)
            pygame.display.update()
            # 피아노(건반) 출력

            for key in keypress:
                self.set_key1_to_octave(key[3])
                self.set_key2_to_octave(key[4])
                while key[2] > pygame.time.get_ticks() - click_time:
                    pass
                if key[0] == 1:  # 키가 눌러짐
                    # 피아노 연주 입력
                    for char in all_possible_key_input:
                        if key[1] == char:
                            if (pressed_keys[char][0] == False):
                                pressed_keys[char][1] = True
                            pressed_keys[char][0] = True
                    # 키보드 셋팅 변경:
                    # ctrl + 숫자패드 ==> z부터 시작하는 키보드 입력 옥타브 변경
                    # alt + 숫자패드 ==>  q부터 시작하는 키보드 입력 옥타브 변경
                if key[0] == 0:  # 키 눌렀다가 떼면 건반 누르기 종료
                    for char in all_possible_key_input:
                        if key[1] == char:
                            if (pressed_keys[char][0]):
                                pressed_keys[char][1] = True
                            pressed_keys[char][0] = False

                # 소리 출력

                self.sound_piano(pressed_keys)
                self.draw(pressed_keys)
                pygame.display.update()  # 화면 update
                for char in keyboard_white_input1 + keyboard_white_input2 + keyboard_black_input1 + keyboard_black_input2:
                    pressed_keys[char][1] = False
            break


    #(F1 or F2) + (키패드 숫자) 입력으로 키보드 셋팅 변경
    def set_key1_to_octave(self, keypad_input):
        self.__set_octave1 = keypad_input - 1
    def get_octave1(self):
        return self.__set_octave1

    def set_key2_to_octave(self, keypad_input):
        self.__set_octave2 = keypad_input - 1

    def get_octave2(self):
        return self.__set_octave2