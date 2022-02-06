import sys, pygame, time, random, tentacle, math
from random import randint


pygame.init()


FPS=60
SPEED=10
WIDTH, HEIGHT = 900,500
middleX, middleY=900/2,500/2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kinematics")
background_color = (0,0,0)


def draw_window():
    global background_color
    pygame.display.update()
    screen.fill(background_color)

class Segment():
    

    
    def __init__(self, *args):#(xPos, yPos, len, angle)  or (Head, len, angle)
        
        if len(args)==4:
            self.list = ["The head is ", self]
            print(self.list, )

            self.xPos = args[0]
            self.yPos = args[1]
            self.len = args[2]
            
            self.angle = math.radians(args[3])
            self.xVariation= self.len * math.cos(self.angle)
            self.yVariation= self.len * math.sin(self.angle)
            
            self.xPos2 = self.xPos+self.xVariation
            self.yPos2 = self.xPos+self.yVariation

            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos, self.yPos2))

        elif len(args)==3:
            args[0].list.append(self)
            print(args[0].list)
            self.xPos = args[0].xPos
            self.yPos = args[0].yPos
            self.len = args[2]
            # self.xPos2, self.yPos2 = findPos2(self.xPos, self.yPos, self.len, self.angle)
            self.angle = math.radians(args[2])
            self.xVariation= self.len * math.cos(self.angle)
            self.yVariation= self.len * math.sin(self.angle)
            
            self.xPos2 = self.xPos+self.xVariation
            self.yPos2 = self.xPos+self.yVariation

            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos, self.yPos2))

    def findPos2(X, Y, length, angle):
        A = length * math.cos(angle)
        B= length * math.sin(angle)
        return (X+A, Y+B)


    def update(self, x, y):
        self.xPos = x
        self.yPos = y
        self.xVariation= len * math.cos(self.angle)
        self.yVariation= len * math.sin(self.angle)

        self.xPos2 = self.xPos+self.xVariation
        self.yPos2 = self.xPos+self.yVariation
        
        pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos2, self.yPos2))

    def show(self, x, y):
        self.xPos2 = x
        self.yPos2 = y
        pygame.draw.line(screen, (0,255,255), (x, y), (x+self.xVariation, y+self.yVariation))





jack = Segment(0, 0, 40, 90)
steve = Segment(jack, 40, 45)
steven = Segment(0, 0, 40, 90)
maker = Segment(jack, 40, 45)

def make_thing(x, y):
    jack.show(x, y)
    steve.show(jack.xPos2, jack.yPos2)
    steven.show(x, y)
    maker.show(steven.xPos2, steven.yPos2)


def main():
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        x, y =pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        draw_window()
        make_thing(x, y)
    pygame.quit()


if __name__ == "__main__":
    main()