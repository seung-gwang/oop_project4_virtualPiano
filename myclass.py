import pygame

class key:
    def __init__(self, image, x, y):
        self.img = image #출력될 키보드 이미지
        self.posX = x #건반 x좌표
        self.posY = y #건반 y좌표

    def make_sound(self): #소리출력
        pass

    def draw(self, screen):
        screen.blit(self.img, (self.posX, self.posY))

    def pressed(self):
        self.img = self.img_pressed



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

                k = key(drawn_image, x=marginX + (7 * whiteKey_width * i) + whiteKey_width * noteIdx,
                        y=int(marginY * 0.7))
                k.draw(self.screen)

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

