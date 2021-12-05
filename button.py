import pygame

class Button():
    def __init__(self, screen, image, act_image, activation, x_pos, y_pos):
        # main_font = pygame.font.SysFont("system", 40)
        self.screen = screen
        self.image = image
        self.act_image = act_image
        self.activation = activation
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))


    def draw(self):
        if self.activation:
            self.screen.blit(self.act_image, (self.x_pos, self.y_pos))
        else:
            self.screen.blit(self.image, (self.x_pos, self.y_pos))

class recording_Button(Button):
    def checkForInput(self, position, record, keypress):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.activation = not self.activation
            if record:#False로 변할 경우 keypress 파일에 입력
                firstTime = keypress[0][2]
                keypress_copy = keypress[:]

                for p in keypress_copy:
                    p[2] -= firstTime
                with open("t1.txt", "w") as file:
                    for i in range(len(keypress)):
                        file.write(str(keypress[i]) + '\n')
                file.close()
            print("recording Button press!")

            return not record #return False

        return record

class play_Button(Button):
    def __init__(self, screen, image, act_image, activation, x_pos, y_pos, obj): #obj는 piano 객체
        self.screen = screen
        self.image = image
        self.act_image = act_image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.activation = activation
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.obj = obj

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):

            print("replay Button press!")

            for i in range(2):
                tempTime = pygame.time.get_ticks()
                running = True
                keypress = []
                with open("sp.txt", "r") as file:
                    keypress = [eval(line.rstrip()) for line in file]
                file.close()
                self.obj.replay(running, keypress, tempTime)


class replay_Button(Button):
    def __init__(self, screen, image, act_image, activation, x_pos, y_pos, obj): #obj는 piano 객체
        self.screen = screen
        self.image = image
        self.act_image = act_image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.activation = activation
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.obj = obj

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("replay Button press!")
            tempTime = pygame.time.get_ticks()
            running = True
            keypress = []
            with open("t1.txt", "r") as file:
                keypress = [eval(line.rstrip()) for line in file]
            file.close()
            self.obj.replay(running, keypress, tempTime)
            return True
        return False

