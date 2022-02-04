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
    def __init__(self, position1, len, angle):
        self.position1 = position1
        self.len = len
        self.angle = math.radians(angle)
        dx= len * math.cos(self.angle)
        dy= len * math.sin(self.angle)
        self.position2 = (self.position1[0]+dx, self.position1[1]+dy)

    def show(self):
        pygame.draw.line(screen, (0,255,255), self.position1, self.position2)


def make_thing(x, y):
    jack = Segment((x, y), 40, 90)
    jack.show()


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

#I want 