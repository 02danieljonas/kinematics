import sys, pygame, time, random, tentacle, math
from random import randint


pygame.init()


FPS=600
SPEED=10
WIDTH, HEIGHT = 900,500
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
    def __init__(self, *args):#(self, xPos, yPos, length, angle)  or (self, master, length, angle)
        
        if len(args)==4:
            self.list = [self]
            self.xPos = args[0]
            self.yPos = args[1]
            self.length = args[2]
            
            self.angle = math.radians(args[3])
            self.xVariation= self.length * math.cos(self.angle)
            self.yVariation= self.length * math.sin(self.angle)
            
            self.xPos2 = self.xPos+self.xVariation
            self.yPos2 = self.xPos+self.yVariation

            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos, self.yPos2))

        elif len(args)==3:
            args[0].list.append(self)
            self.xPos = args[0].xPos2
            self.yPos = args[0].yPos2
            self.length = args[1]
            # self.xPos2, self.yPos2 = findPos2(self.xPos, self.yPos, self.length, self.angle)
            self.angle = math.radians(args[2])
            self.xVariation= self.length * math.cos(self.angle)
            self.yVariation= self.length * math.sin(self.angle)
            
            self.xPos2 = self.xPos+self.xVariation
            self.yPos2 = self.xPos+self.yVariation

            pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos2, self.yPos2))


    def findPos2(X, Y, length, angle):
        A = length * math.cos(angle)
        B = length * math.sin(angle)
        return (X+A, Y+B)


    def update(self, x, y):
        self.xPos = x
        self.yPos = y
        self.xVariation= self.length * math.cos(self.angle)
        self.yVariation= self.length * math.sin(self.angle)

        self.xPos2 = self.xPos+self.xVariation
        self.yPos2 = self.xPos+self.yVariation
        
        pygame.draw.line(screen, (0,255,255), (self.xPos, self.yPos), (self.xPos2, self.yPos2))
    def move(x, y):
        pass
        #to move self.xpos += speed to which ever direction you want
        #to move self.ypos += speed to which ever direction you want

    def show(self, x, y):
        for item in self.list:
            item.xPos = x
            item.yPos = y
            item.xPos2 = item.xPos+item.xVariation
            item.yPos2 = item.yPos+item.yVariation
            pygame.draw.line(screen, (0,255,255), (item.xPos, item.yPos), (item.xPos2, item.yPos2))
            y = item.yPos2
            x = item.xPos2


jack = Segment(0, 0, 40, 45)
steve = Segment(jack, 40, 90)

# steven = Segment(0, 0, 40, 3.14)
# maker = Segment(steven, 40, 4.71239)

def make_thing(x, y):
    jack.show(x, y)
    # steve.show(jack.xPos2, jack.yPos2)
    # steven.show(x, y)
    # maker.show(steven.xPos2, steven.yPos2)


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