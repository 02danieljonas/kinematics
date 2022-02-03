import sys, pygame, time, random
from random import randint
pygame.init()

FPS=60
WIDTH, HEIGHT = 900,500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kinematics")

def draw_window():
    WIN.fill(0,0,0)
    pygame.display.update()

def main():
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()