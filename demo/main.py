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
    def __init__(self, *args):#(self, xPos, yPos, length, angle, speed)  or (self, parent, length, angle, speed)
        
        if len(args)==5:
            self.list = [self]
            self.xPos = args[0]
            self.yPos = args[1]
            self.length = args[2]
            self.speed = args[4]
            self.angle = math.radians(args[3])
            self.findPos2()
            
            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos, self.yPos2))

        elif len(args)==4:
            args[0].list.append(self)
            self.xPos = args[0].xPos2
            self.yPos = args[0].yPos2
            self.length = args[1]
            self.speed = args[3]
            self.angle = math.radians(args[2])
            self.findPos2()

            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos2, self.yPos2))


    def findPos2(self):
        self.xVariation = self.length * math.cos(self.angle)
        self.yVariation = self.length * math.sin(self.angle)
        self.xPos2=self.xVariation+self.xPos
        self.yPos2=self.yVariation+self.yPos
    
    def findObject(self, xTarget, yTraget):
        pass


    def move(self, xMoveTo, yMoveTo):
        if (self.yPos-yMoveTo)!=0 and (self.xPos-xMoveTo)!=0:
            print(self.yPos-yMoveTo, self.xPos-xMoveTo)
            slope = (self.yPos-yMoveTo)/(self.xPos-xMoveTo)
            #TODO: make it follow a straight line, instead of moving x and y independently, use maths from HS
            if self.xPos-xMoveTo<=-self.speed: LorR=1
                # self.xPos+=self.speed #moves it to the right
            elif self.xPos-xMoveTo>=self.speed: LorR=-1
                # self.xPos-=self.speed #moves it to the left
            else: LorR=0
                # self.xPos=xMoveTo #teleports it to position
                
            
            if self.yPos-yMoveTo<=-self.speed:UorD=1
                # self.yPos+=self.speed #moves it up
            elif self.yPos-yMoveTo>=self.speed:UorD=-1
                # self.yPos-=self.speed #moves it down
            else:UorD=0
                # self.yPos=yMoveTo #teleports it to position

            if LorR == 1 and UorD == 1:
                pass
        else:
            self.xPos=xMoveTo #teleports it to position
            self.yPos=yMoveTo #teleports it to position


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