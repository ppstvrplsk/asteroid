import pygame
from constants import *

def main():
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill("black",rect=None, special_flags=0)
        pygame.display.flip()

if __name__ == "__main__":
    main()