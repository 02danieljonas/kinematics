import sys, pygame, time, random, math, numpy
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

class Segment():
    def __init__(self, *args):#(self, xPos, yPos, length, angle, speed)  or (self, captain, parent, length, angle, speed)
        """To create the starting segment pass the XPosition Yposition, the length, angle and speed
        To create a child pass a starting segment, length, angle and speed
        """        
        if isinstance(args[0], float) or isinstance(args[0], int): #(self, xPos, yPos, length, angle, speed)
            self.list = [self]
            self.xPos = args[0]
            self.yPos = args[1]
            self.length = args[2]
            self.speed = args[4]/200
            self.angle = math.radians(args[3])
            self.findPos2()            
            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos, self.yPos2))
            
        elif isinstance(args[0], Segment): #(self, captain, parent, length, angle, speed) change to (self, captain, length, angle, speed)
            self.captain = args[0]
            self.captain.list.append(self)
            self.parent = self.captain.list[len(self.captain.list)-2]
            self.xPos = self.parent.xPos2
            self.yPos = self.parent.yPos2
            self.length = args[1]
            self.speed = args[3]/200

            self.realAngle = math.radians(args[2])#this is the actualy angle value
            self.angle = self.realAngle + self.parent.angle#this is the angle relative to its parent

            self.findPos2()
            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos2, self.yPos2))
        else:
            raise Exception("Incorrect Format")

    def findPos2(self):
        xVariation = self.length * math.cos(self.angle)
        yVariation = self.length * math.sin(self.angle)
        self.xPos2=xVariation+self.xPos
        self.yPos2=yVariation+self.yPos
    
    def followParent(self):
        self.xPos = self.parent.xPos2
        self.yPos = self.parent.yPos2
        self.realAngle+=self.speed
        print(self.speed)
        self.angle = self.realAngle + self.parent.angle
        self.findPos2()
    
    def update(self):
        for self in self.list:
            if not hasattr(self, "captain"):
                self.angle+=self.speed
                self.findPos2()
                pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos2, self.yPos2))
            else:
                self.followParent()
                self.findPos2()
                pygame.draw.line(screen, (0,255,0), (self.xPos, self.yPos), (self.xPos2, self.yPos2))

jack = Segment(WIDTH/2, HEIGHT/2, 40, 90, 2)
pete = Segment(jack, 50, 90, 0)

def draw_window():
    global background_color
    pygame.display.update()
    screen.fill(background_color)

def make_thing(x, y):
    jack.update()

def main():
    run = True
    from time import time
    startTime = time()
    print(startTime)
    
    while run:
        pygame.time.Clock().tick(FPS)
        x, y =pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        draw_window()
        # print("The first values are ", x, y)
        make_thing(x, y)
        if (not pygame.display.get_active()) and (time()-startTime>4):
            run=False

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Closing")