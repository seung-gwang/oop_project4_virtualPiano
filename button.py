import pygame

class Button():
    def __init__(self, screen, image,  x_pos, y_pos, obj):
        # main_font = pygame.font.SysFont("system", 40)
        self._screen = screen
        self._image = image
        #self._act_image = act_image
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._obj = obj
        self._rect = self._image.get_rect(center = (self._x_pos, self._y_pos))


    def draw(self):
            self._screen.blit(self._image, (self._x_pos, self._y_pos))

class recording_Button(Button):
    def __init__(self, screen, image, act_image, activation, x_pos, y_pos):
        # main_font = pygame.font.SysFont("system", 40)
        self.__screen = screen
        self.__image = image
        self.__act_image = act_image
        self.__activation = activation
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        self.__rect = self.__image.get_rect(center = (self.__x_pos, self.__y_pos))

    def checkForInput(self, position, record, keypress):
        if position[0] in range(self.__rect.left, self.__rect.right) and position[1] in range(self.__rect.top, self.__rect.bottom):
            self.__activation = not self.__activation
            if record:#False로 변할 경우 keypress 파일에 입력
                firstTime = keypress[0][2]
                keypress_copy = keypress[:]

                for p in keypress_copy:
                    p[2] -= firstTime
                with open("t1.txt", "w") as file:
                    for i in range(len(keypress)):
                        file.write(str(keypress[i]) + '\n')
                file.close()

            return not record #return False

        return record

    def draw(self):
        if self.__activation:
            self.__screen.blit(self.__act_image, (self.__x_pos, self.__y_pos))
        else:
            self.__screen.blit(self.__image, (self.__x_pos, self.__y_pos))

class play_Button(Button):
    def __init__(self, screen, image, x_pos, y_pos, obj):
        Button.__init__(self, screen, image, x_pos, y_pos, obj)

    def checkForInput(self, position):
        if position[0] in range(self._rect.left, self._rect.right) and position[1] in range(self._rect.top,
                                                                                          self._rect.bottom):


            for i in range(2):
                tempTime = pygame.time.get_ticks()
                running = True
                keypress = []
                with open("sp.txt", "r") as file:
                    keypress = [eval(line.rstrip()) for line in file]
                file.close()
                self._obj.replay(running, keypress, tempTime)


class replay_Button(Button):

    # def __init__(self, screen, image, act_image, x_pos, y_pos, obj): #obj는 piano 객체
    #     self.__screen = screen
    #     self.__image = image
    #     self.__act_image = act_image
    #     self.__x_pos = x_pos
    #     self.__y_pos = y_pos
    #     #self.activation = activation
    #     self.__rect = self.__image.get_rect(center = (self.__x_pos, self.__y_pos))
    #     self.__obj = obj
    def __init__(self, screen, image, x_pos, y_pos, obj):
        Button.__init__(self, screen, image, x_pos, y_pos, obj)

    def checkForInput(self, position):
        if position[0] in range(self._rect.left, self._rect.right) and position[1] in range(self._rect.top, self._rect.bottom):
            tempTime = pygame.time.get_ticks()
            running = True
            keypress = []
            with open("t1.txt", "r") as file:
                keypress = [eval(line.rstrip()) for line in file]
            file.close()
            self._obj.replay(running, keypress, tempTime)
            return True
        return False

