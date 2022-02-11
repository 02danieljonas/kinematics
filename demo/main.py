import sys, pygame, time, random, math, numpy
from random import randint

#C:\Users\Daniel\Desktop\Programs\Python\Programming\kinematics\kinematics_venv\Scripts\python.exe C:\Users\Daniel\Desktop\Programs\Python\Programming\kinematics\kinematics_venv\Scripts\pip.exe install ~~~

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
        
        if isinstance(args[0], float) or isinstance(args[0], int): #(self, xPos, yPos, length, angle, speed)
            self.list = [self]
            self.xPos = args[0]
            self.yPos = args[1]
            self.length = args[2]
            self.speed = args[4]
            self.angle = math.radians(args[3])
            self.findPos2()            
            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos, self.yPos2))
            
        elif isinstance(args[0], Segment): #(self, parent, length, angle, speed) change it to (self, captain, parent, length, angle, speed)
            self.captain = args[0]
            args[0].list.append(self)
            self.parent = args[1]
            self.xPos = self.parent.xPos2
            self.yPos = self.parent.yPos2
            self.length = args[2]
            self.speed = args[4]
            self.angle = math.radians(args[3])
            self.findPos2()
            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos2, self.yPos2))
        else:
            raise Exception("Incorrect Format")


    def findPos2(self):
        self.xVariation = self.length * math.cos(self.angle)
        self.yVariation = self.length * math.sin(self.angle)
        self.xPos2=self.xVariation+self.xPos
        self.yPos2=self.yVariation+self.yPos
    
    
    def findObject(self, xTarget, yTraget):
        
        if hasattr(self, "parent"):
            self.xPos=self.parent.xPos2
            self.yPos=self.parent.yPos2
            self.angle += self.speed + self.parent.angle
        else:
            self.angle +=self.speed
        
        self.findPos2()

    def findVectorAngle(self, xTarget, yTarget):

        # print("xTarget2 is ", xTarget)
        # print("yTraget2 is ", yTarget)

        u = (self.xPos-self.xPos+0.0000000001, self.yPos-self.yPos+0.0000000001)
        # print("us is ", u)
        v = (self.xPos2-xTarget+0.0000000001, self.xPos2-yTarget+0.0000000001)
        # print("v is ", v)

        uv = (u[0]*v[0]+u[1]*v[1])
        # print("uv is ", uv)

        uMagnitude = math.sqrt(math.pow(u[0],2) + math.pow(u[1], 2))
        # print("uMagnitude is ", uMagnitude)

        vMagnitude = math.sqrt(math.pow(v[0],2) + math.pow(v[1], 2))
        # print("vMagnitude is ", vMagnitude)

        self.angle = math.degrees(math.acos(uv/(uMagnitude*vMagnitude+0.0000000001)))
        # print("self.angle is ", self.angle)


    def move(self, xMoveTo, yMoveTo):
        if (self.yPos-yMoveTo)!=0 and (self.xPos-xMoveTo)!=0:
            # print(self.yPos-yMoveTo, self.xPos-xMoveTo)
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
            # print("x is ", x)
            # print("y is ", y)
            
            self.findObject(x, y)
            
            x = self.xPos2
            y = self.yPos2
            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos2, self.yPos2))


jack = Segment(WIDTH/2, HEIGHT/2, 40, 45, .01)
pete = Segment(jack, jack, 40, 90, .0)
# peter = Segment(jack, pete, 10, 0, .0)
# peter = Segment(jack, peter, 20, 10, .0)
# peter = Segment(jack, peter, 40, 20, .0)
# peter = Segment(jack, peter, 60, 30, .0)


# steve = Segment(WIDTH/4, HEIGHT/2, 40, 45, .01)
# stev = Segment(steve, 40, 90, .01)#found an error can't connect code like this


def draw_window():
    global background_color
    pygame.display.update()
    screen.fill(background_color)

def make_thing(x, y):
    jack.show(x, y)
    # steve.show(x,y)


def main():
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        x, y =pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        draw_window()
        # print("The first values are ", x, y)
        make_thing(x, y)
    pygame.quit()


if __name__ == "__main__":
    main()