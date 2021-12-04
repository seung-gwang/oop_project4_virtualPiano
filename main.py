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

# title 삽입
title = pygame.image.load("title.png")
background.blit(title, [400, 40])
#버튼 배경 이미지 불러오기
button_surface = pygame.image.load("button.png")

pygame.init()#pygame 초기화
p = piano(screen) #피아노 객체 생성

#버튼 객체 생성
recording = recording_Button(screen, button_surface, 450, 440, "record")
play = play_Button(screen, button_surface, 650, 440, "play")
pause = pause_Button(screen, button_surface, 850, 440, "pause")
notes = notes_Button(screen, button_surface, 1050, 440, "notes")

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

record = False
keypress = []

#event loop ==> 피아노의 화면 출력 갱신
running = True
while running:
    #이벤트 검사
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #while loop 탈출: 창 닫고 프로그램 종료
            running = False
        if event.type == pygame.KEYDOWN: #키가 눌러짐


            # 피아노 연주 입력
            if record == True:
                keypress.append([1, str(event.unicode), pygame.time.get_ticks()])
            for char in all_possible_key_input:
                if event.key == pygame.key.key_code(char):
                    if record == True:

                        keypress.append(
                            [1, str(event.unicode), pygame.time.get_ticks(), p.set_octave1 + 1, p.set_octave2 + 1])
                    if (pressed_keys[char][0] == False):
                        pressed_keys[char][1] = True
                    pressed_keys[char][0] = True
            #키보드 셋팅 변경:
            #ctrl + 숫자패드 ==> z부터 시작하는 키보드 입력 옥타브 변경
            # alt + 숫자패드 ==>  q부터 시작하는 키보드 입력 옥타브 변경
            keypad_input = 0
            if event.mod & pygame.KMOD_CTRL:
                if event.key == pygame.K_KP1:
                    keypad_input = 1
                elif event.key == pygame.K_KP2:
                    keypad_input = 2
                elif event.key == pygame.K_KP3:
                    keypad_input = 3
                elif event.key == pygame.K_KP4:
                    keypad_input = 4
                elif event.key == pygame.K_KP5:
                    keypad_input = 5
                elif event.key == pygame.K_KP6:
                    keypad_input = 6
                elif event.key == pygame.K_KP7:
                    keypad_input = 7

            if event.mod & pygame.KMOD_ALT:
                if event.key == pygame.K_KP1:
                    keypad_input = 1
                elif event.key == pygame.K_KP2:
                    keypad_input = 2
                elif event.key == pygame.K_KP3:
                    keypad_input = 3
                elif event.key == pygame.K_KP4:
                    keypad_input = 4
                elif event.key == pygame.K_KP5:
                    keypad_input = 5
                elif event.key == pygame.K_KP6:
                    keypad_input = 6
                elif event.key == pygame.K_KP7:
                    keypad_input = 7

        if event.type == pygame.KEYUP: #키 눌렀다가 떼면 건반 누르기 종료

            if record == True:
                keypress.append([0, str(event.unicode), pygame.time.get_ticks()])

            for char in all_possible_key_input:
                if event.key == pygame.key.key_code(char):
                    if record == True:
                        keypress.append(
                            [0, str(event.unicode), pygame.time.get_ticks(), p.set_octave1 + 1, p.set_octave2 + 1])
                    if (pressed_keys[char][0]):
                        pressed_keys[char][1] = True
                    pressed_keys[char][0] = False

            if event.mod & pygame.KMOD_CTRL:
                p.set_key1_to_octave(keypad_input)
            if event.mod & pygame.KMOD_ALT:
                p.set_key2_to_octave(keypad_input)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Button.checkForInput(pygame.mouse.get_pos())
            record = recording.checkForInput(pygame.mouse.get_pos(),record, keypress)
            print(record)
            play.checkForInput(pygame.mouse.get_pos())
            pause.checkForInput(pygame.mouse.get_pos())
            notes.checkForInput(pygame.mouse.get_pos())

        # 소리 출력
        p.sound_piano(pressed_keys)

        for char in keyboard_white_input1 + keyboard_white_input2 + keyboard_black_input1 + keyboard_black_input2:
            pressed_keys[char][1] = False

    #배경 출력
    screen.blit(background, (0,0))
    #버튼 업데이트/출력
    recording.update()
    recording.changecolor(pygame.mouse.get_pos())

    play.update()
    play.changecolor(pygame.mouse.get_pos())

    pause.update()
    pause.changecolor(pygame.mouse.get_pos())

    notes.update()
    notes.changecolor(pygame.mouse.get_pos())

    #피아노(건반) 출력
    p.draw(pressed_keys)
    pygame.display.update()  # 화면 update



# keypress.append([0, "0", 0, 0, 0]) #더미 데이터
# with open("t1.txt", "w") as file:
#     for i in range(len(keypress)):
#         file.write(str(keypress[i]) + '\n')
file.close()

#프로그램 종료
pygame.quit()