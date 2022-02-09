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
        xDistanceTo = self.xPos - xTarget
        yDistanceTo = self.yPos - yTraget
        c = math.sqrt((xDistanceTo*xDistanceTo)+(yDistanceTo*yDistanceTo))
        D=yDistanceTo/c

        self.angle = -numpy.arcsin(D)

        print("xTarget1 is ", xTarget)
        print("yTraget1 is ", yTraget)
        
        self.findVectorAngle(xTarget, yTraget)

        self.findPos2()

    def findVectorAngle(self, xTarget, yTarget):

        print("xTarget2 is ", xTarget)
        print("yTraget2 is ", yTarget)

        u = (self.xPos2-self.xPos+0.0000000001, self.yPos2-self.yPos+0.0000000001)
        print("us is ", u)
        v = (xTarget-self.xPos+0.0000000001, yTarget-self.xPos+0.0000000001)
        print("v is ", v)

        uv = (u[0]*v[0]+u[1]*v[1])
        print("uv is ", uv)

        uMagnitude = math.sqrt(math.pow(u[0],2) + math.pow(u[1], 2))
        print("uMagnitude is ", uMagnitude)

        vMagnitude = math.sqrt(math.pow(v[0],2) + math.pow(v[1], 2))
        print("vMagnitude is ", vMagnitude)

        self.angle = math.degrees(math.acos(uv/(uMagnitude*vMagnitude)))
        print("self.angle is ", self.angle)

        
        
        
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
            print("x is ", x)
            print("y is ", y)

            self.findObject(x, y)
            x = self.xPos2 = self.xPos+self.xVariation
            y = self.yPos2 = self.yPos+self.yVariation
            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos2, self.yPos2))


jack = Segment(WIDTH/2, HEIGHT/2, 40, 45, 6)
# steve = Segment(jack, 40, 90, 6)


def draw_window():
    global background_color
    pygame.display.update()
    screen.fill(background_color)

def make_thing(x, y):
    jack.show(x, y)


def main():
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        x, y =pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        draw_window()
        print("The first values are ", x, y)
        make_thing(x, y)
    pygame.quit()


if __name__ == "__main__":
    main()