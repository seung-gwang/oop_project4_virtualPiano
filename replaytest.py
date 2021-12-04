import pygame
from myclass import *

#화면 크기 설정
screen_width = 1600 #창 가로 길이
screen_height = 800 #창 세로 길이
screen = pygame.display.set_mode((screen_width, screen_height))

#Title
pygame.display.set_caption("virtual piano")

#background 이미지 불러오기
background = pygame.image.load("background.png")

pygame.init()#pygame 초기화
p = piano(screen) #피아노 객체 생성

#가능한 키보드 입력 설정
keyboard_white_input1 = "zxcvbnm"
keyboard_black_input1 = "sdfghjk"
keyboard_white_input2 = "qwertyu"
keyboard_black_input2 = "2345678"
all_possible_key_input = keyboard_white_input1 + keyboard_black_input1 + keyboard_white_input2 + keyboard_black_input2

#입력된 키보드 값 저장할 딕셔너리 False(건반 눌려지지 않음)으로 초기화
pressed_keys = dict()

for char in keyboard_white_input1 + keyboard_white_input2 + keyboard_black_input1 + keyboard_black_input2:
    pressed_keys[char] = [False, False]

keypress = []
with open("t1.txt", "r") as file:
    keypress = [eval(line.rstrip()) for line in file]
file.close()

#event loop ==> 피아노의 화면 출력 갱신
running = True
while running:
    screen.blit(background, (0, 0))
    p.draw(pressed_keys)
    pygame.display.update()
    # 피아노(건반) 출력

    for key in keypress:
        p.set_key1_to_octave(key[3])
        p.set_key2_to_octave(key[4])
        while key[2] > pygame.time.get_ticks():
            print("wait")
        if key[0] == 1: #키가 눌러짐
            #피아노 연주 입력
            for char in all_possible_key_input:
                if key[1] == char:
                    if (pressed_keys[char][0] == False):
                        pressed_keys[char][1] = True
                    pressed_keys[char][0] = True
            #키보드 셋팅 변경:
            #ctrl + 숫자패드 ==> z부터 시작하는 키보드 입력 옥타브 변경
            # alt + 숫자패드 ==>  q부터 시작하는 키보드 입력 옥타브 변경
        if key[0] == 0: #키 눌렀다가 떼면 건반 누르기 종료
            for char in all_possible_key_input:
                if key[1] == char:
                    if(pressed_keys[char][0]):
                        pressed_keys[char][1] = True
                    pressed_keys[char][0] = False

        # 소리 출력

        p.sound_piano(pressed_keys)
        p.draw(pressed_keys)
        pygame.display.update()  # 화면 update
        for char in keyboard_white_input1 + keyboard_white_input2 + keyboard_black_input1 + keyboard_black_input2:
            pressed_keys[char][1] = False

    break

#프로그램 종료
pygame.quit()