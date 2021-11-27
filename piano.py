from tkinter import*
import time
import datetime
import pygame
#import numpy as np

class key:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        self.keyboard_input = None  # 인식할 키보드 입력
        mouse = pygame.mouse.get_pos() #마우스 좌표
        click = pygame.mouse.get_pressed() #클릭


        if (x< mouse[0] < x + width) and (y <  mouse[1] < y + height) and click:#건반 클릭
            gameDisplay.blit(img_act, (x, y))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            gameDisplay.blit(img_in, (x, y))
    def bind_key_to_keyboard(self, keyboard):
        self.keyboard_input = keyboard


class piano:
    whiteKeys = list()
    blackKeys = list()

    def __init__(self, whiteKeyImg, blackKeyImg, whiteKeyPressedImg, blackKeyPressedImg,  o_num = 7, s_type = 1):
        self.octave_num = o_num #기본 2옥타브 피아노
        self.sound_type = s_type #기본 type 1 소리
        self.white_key_default = whiteKeyImg
        self.black_key_default = blackKeyImg
        self.white_key_pressed = whiteKeyPressedImg
        self.black_key_pressed = blackKeyPressedImg

    def draw(self):
        # for i in range(self.octave_num):
        #
        whiteKeys = ['C', 'D', 'E', 'F', 'G', 'A', 'B']  # 도 레 미 파 솔 라 시
        blackKeys = ['Cs', 'Ds', 'dummy', 'Fs', 'Gs', 'As',
                     'dummy']  # 도# 레# 파# 솔# 라#, dummy는 미-파, 시-도 반음 사이에 위치하는 없는 건반
        whiteWidth = int(1600 / self.octave_num / 7)  # 가로 창 길이 / 옥타브 수 / 한 옥타브당 흰 건반 수
        whiteHeight = int(whiteWidth * 4)
        blackWidth = int(whiteWidth * 0.5)
        blackHeight = int(blackWidth * 5)
        marginX = 150
        marginY = 150

        displayWidth = 1800
        displayHeight = 800
        gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
        pygame.display.set_caption("virtual piano")

        clock = pygame.time.Clock()

        #pygame.init()
        # root = Tk()
        # root.title('Virtual Piano')
        # root.geometry('1600x800+0+0')
        # root.configure(background='white')


        # ABC = Frame(root, bg="#6B3922", bd=5, relief=RIDGE)
        # ABC.grid()
        #
        #
        # ABC1 = Frame(ABC, bg="#6B3922", bd=5, relief=RIDGE)
        # ABC1.grid()
        #
        # ABC2 = Frame(ABC, bg="#6B3922", bd=5, relief=RIDGE, width = 7*self.octave_num*whiteWidth+marginX, height = whiteHeight+marginY)
        # ABC2.grid()
        #
        #
        # Label(ABC1, text="Virtual Piano",
        #       font=('Segoe Script', 70, 'bold', 'italic'),
        #       padx=8, pady=8, bd=4, bg="#6B3922",
        #       fg="white", justify=CENTER).grid(row=0, column=0, columnspan=11)

        #------------------------------------------------------건반 출력-------------------------------------------------
        # def print_line(event=""):
        #     print("print line")
        #btnList = list()
        gameDisplay.fill((255,255,255))#white background

        white_key_default = pygame.transform.scale(self.white_key_default, (whiteWidth, whiteHeight))
        white_key_pressed = pygame.transform.scale(self.white_key_pressed, (whiteWidth, whiteHeight))
        black_key_default = pygame.transform.scale(self.black_key_default, (blackWidth, blackHeight))
        black_key_pressed = pygame.transform.scale(self.black_key_pressed, (blackWidth, blackHeight))
        # whiteKey = key(img_in=white_key_default,
        #                x=200,
        #                y=300,
        #                width=whiteWidth,
        #                height=whiteHeight,
        #                img_act=white_key_pressed,
        #                x_act=200,
        #                y_act=300
        #                )




        for i in range(self.octave_num):#옥타브별

            for keyIdx in range(len(whiteKeys)): #백건 출력
                whiteKey = key(img_in=white_key_default,
                               x= (7*whiteWidth*i)+whiteWidth*keyIdx + marginX * 0.5,
                               y= int(marginY * 0.7),
                               width= whiteWidth,
                               height= whiteHeight,
                               img_act= white_key_pressed,
                               x_act= (7*whiteWidth*i)+whiteWidth*keyIdx + int(marginX * 0.5),
                               y_act= int(marginY * 0.7)
                               )
                whiteKeys.append(whiteKey)

            for keyIdx in range(len(blackKeys)): #흑건 출력
                if (blackKeys[keyIdx] != 'dummy'):
                    blackKey = key(img_in=black_key_default,
                                   x = (7*whiteWidth*i)+(keyIdx+1)*whiteWidth-0.5*blackWidth + int(marginX*0.5),
                                   y=marginY*0.7,
                                   width= blackWidth,
                                   height= blackHeight,
                                   img_act= black_key_pressed,
                                   x_act= (7*whiteWidth*i)+(keyIdx+1)*whiteWidth-0.5*blackWidth + int(marginX*0.5),
                                   y_act= int(marginY * 0.7)
                                   )
                    blackKeys.append(blackKey)


        #건반 생성 후 키보드와 건반을 bind
        octave1_white_keys = "zxcvbnm"
        octave1_black_keys = "sdghj"
        octave2_white_keys = "qwertyu"
        octave2_black_keys = "23567"

        for i in range(len(octave1_white_keys)):
            whiteKeys[i].bind_key_to_keyboard(octave1_white_keys[i])
            whiteKeys[i+7].bind_key_to_keyboard(octave2_white_keys[i])
        for i in range(len(octave1_black_keys)):
            blackKeys[i].bind_key_to_keyboard(octave1_black_keys[i])
            blackKeys[i + 7].bind_key_to_keyboard(octave2_black_keys[i])

            #바인딩 변경 메소드 나중에 추가 필요

            #pygame.display.update()
                # whiteKey = key(img_in = self.white_key_default,
                #                x = (7*whiteWidth*i)+whiteWidth*keyIdx + int(marginX * 0.5),
                #                y = int(marginY * 0.7),
                #                width = whiteWidth,
                #                height = whiteHeight,
                #                img_act = self.white_key_pressed,
                #                x_act = (7*whiteWidth*i)+whiteWidth*keyIdx + int(marginX * 0.5),
                #                y_act = int(marginY * 0.7)
                #                )

        #
        # for i in range(self.octave_num):#옥타브별
        #
        #     for keyIdx in range(len(whiteKeys)): #백건 출력
        #         whiteKey = key(img_in = self.white_key_default,
        #                        x = (7*whiteWidth*i)+whiteWidth*keyIdx + int(marginX * 0.5),
        #                        y = int(marginY * 0.7),
        #                        width = whiteWidth,
        #                        height = whiteHeight,
        #                        img_act = self.white_key_pressed,
        #                        x_act = (7*whiteWidth*i)+whiteWidth*keyIdx + int(marginX * 0.5),
        #                        y_act = int(marginY * 0.7)
        #                        )



            #     btn = Button(ABC2, height=whiteHeight, width=whiteWidth, bd=4, activebackground = 'pink',
            #                  #text = whiteKeys[keyIdx],
            #                  bg='white', fg='black', font=('arial', 18, 'bold'), command=self.sound(i, whiteKeys[keyIdx]))
            #     #btn.append(btn)
            #     btn.bind('<A>', btn.invoke())
            #     btn.place(x = (7*whiteWidth*i)+whiteWidth*keyIdx + int(marginX * 0.5), y = int(marginY * 0.7), width = whiteWidth, height = whiteHeight)
            #
            #
            # for keyIdx in range(len(blackKeys)):  # 흑건 출력
            #     if(blackKeys[keyIdx] != 'dummy'):
            #         btn = Button(ABC2, height=blackHeight, width=blackWidth, bd=4,
            #                      #text=blackKeys[keyIdx],
            #                      bg='black', fg='white', font=('arial', 18, 'bold'), command=self.sound(i, blackKeys[keyIdx]))
            #         #btnList.append(btn)
            #         btn.place(x = (7*whiteWidth*i)+(keyIdx+1)*whiteWidth-0.5*blackWidth + int(marginX*0.5), y=marginY*0.7, width = blackWidth, height = blackHeight)
            #         btn.bind('<S>', btn.invoke())
        #------------------------------------------------------버튼 출력-------------------------------------------------
       #  widgetHeight = int(whiteWidth * 2)
       #  widgetWidth = widgetHeight
       #
       #  micImage = PhotoImage(file="mic.png")
       #  micImageResized = micImage.subsample(10, 10)
       #  micButton = Button(ABC2, height=widgetHeight, width=widgetWidth, bd=4, bg='yellow', fg='black', image = micImageResized )
       #  micButton.place(x=int(self.octave_num * 0.5 * 7 * whiteWidth) - 2 * widgetWidth, y=int(0.3 * marginY * 0.5),
       #                   height=widgetHeight, width=widgetWidth)
       #
       #  playImage = PhotoImage(file = "play.png")
       #  playImageResized = playImage.subsample(10,10)
       #  playButton = Button(ABC2, height = widgetHeight, width = widgetWidth, bd=4, bg = 'yellow', fg='black', image=playImageResized)
       #  playButton.place(x= int(self.octave_num * 0.5 * 7 * whiteWidth), y = int(0.3*marginY*0.5), height = widgetHeight, width = widgetWidth)
       #
       #  stopImage = PhotoImage(file="stop.png")
       #  stopImageResized = stopImage.subsample(10, 10)
       #  stopButton = Button(ABC2, height=widgetHeight, width=widgetWidth, bd=4, bg='yellow', fg='black', image = stopImageResized, command = print_line)
       #  stopButton.place(x=int(self.octave_num * 0.5 * 7 * whiteWidth) + 2*widgetWidth, y=int(0.3 * marginY * 0.5), height = widgetHeight, width = widgetWidth)
       #  stopButton.bind("<S>",self.sound(1,2))
       #
       # # stopButton.invoke()
       #  root.mainloop()


    def sound(self, octave, pitch, event = None):
     # if btnSound == 'Cs': 옥타브와 계이름에 대한 조건 추가 필요
        def value_Cs(self):
            str1 = StringVar()
            str1.set("C#")
            sound = pygame.mixer.Sound("C:\music_piano\C_s.wav")
            sound.play()
        return value_Cs

whiteKeyImg = pygame.image.load("whiteKey.png")
blackKeyImg = pygame.image.load("blackKey.png")
whiteKeyPressedImg = pygame.image.load("whiteKey_pressed.png")
blackKeyPressedImg = pygame.image.load("blackKey_pressed.png")

#p = piano(7)
def display_piano():
    whiteKeyImg = pygame.image.load("whiteKey.png")
    blackKeyImg = pygame.image.load("blackKey.png")
    whiteKeyPressedImg = pygame.image.load("whiteKey_pressed.png")
    blackKeyPressedImg = pygame.image.load("blackKey_pressed.png")

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.fill((255,255,255))

        p = piano(whiteKeyImg, blackKeyImg, whiteKeyPressedImg, blackKeyPressedImg)
        p.draw()
        pygame.display.update()

gameDisplay = pygame.display.set_mode((1600,800))
pygame.init()
display_piano()


