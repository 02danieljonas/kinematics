import sys, pygame, time, random, tentacle, testing
from random import randint
pygame.init()


FPS=60
WIDTH, HEIGHT = 900,500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kinematics")
background_color = (0,0,0)


def draw_window():
    global background_color
    pygame.display.update()
    screen.fill(background_color)


def make_thing(x, y):
    pygame.draw.rect(screen, (0,255,255), pygame.Rect(x, y, 1, 39))


def main():
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        x, y =pygame.mouse.get_pos()
        print(x)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        draw_window()
        make_thing(x, y)
    pygame.quit()


if __name__ == "__main__":
    main()