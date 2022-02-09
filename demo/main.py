import sys, pygame, time, random, tentacle, math
from random import randint

pygame.init()

FPS=600
SPEED=10
WIDTH, HEIGHT = 900,900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kinematics")
background_color = (0,0,0)

SHRINKING_SEGMENT = False
LENGTH = None

def draw_window():
    global background_color
    pygame.display.update()
    screen.fill(background_color)


class Segment():
    def __init__(self, *args):#(self, xPos, yPos, length, angle, speed)  or (self, master, length, angle, speed)
        
        if len(args)==5:
            self.list = [self]
            self.xPos = args[0]
            self.yPos = args[1]
            self.length = args[2]
            self.speed = args[4]
            self.angle = math.radians(args[3])
            self.xVariation, self.yVariation, self.xPos2, self.yPos2 = self.findPos2(self.xPos, self.yPos, self.length, self.angle)
            
            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos, self.yPos2))

        elif len(args)==4:
            args[0].list.append(self)
            self.xPos = args[0].xPos2
            self.yPos = args[0].yPos2
            self.length = args[1]
            self.speed = args[3]
            self.angle = math.radians(args[2])
            self.xVariation, self.yVariation, self.xPos2, self.yPos2 = self.findPos2(self.xPos, self.yPos, self.length, self.angle)

            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos2, self.yPos2))


    def findPos2(Self, X, Y, length, angle):
        A = length * math.cos(angle)
        B = length * math.sin(angle)
        return A, B, X+A, Y+B


    def move(self, xMoveTo, yMoveTo):
        #TODO: make it follow a straight line, instead of moving x and y independently, use maths from HS
        if self.xPos-xMoveTo<=-self.speed:
            self.xPos+=self.speed
        elif self.xPos-xMoveTo>=self.speed:
            self.xPos-=self.speed
        else:
            self.xPos=xMoveTo
        if self.yPos-yMoveTo<=-self.speed:
            self.yPos+=self.speed
        elif self.yPos-yMoveTo>=self.speed:
            self.yPos-=self.speed
        else:
            self.yPos=yMoveTo


    def show(self, x, y):
        for self in self.list:
            #self.move() should be here
            self.move(x, y)
            
            # item.xPos = x
            # item.yPos = y
            x = self.xPos2 = self.xPos+self.xVariation
            y = self.yPos2 = self.yPos+self.yVariation
            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos2, self.yPos2))


jack = Segment(0, 0, 40, 45, 6)
steve = Segment(jack, 40, 90, 6)

steven = Segment(0, 0, 40, 0, 6)
maker = Segment(steven, 40, 0, 6)

def make_thing(x, y):
    jack.show(x, y)
    steven.show(x, y)


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