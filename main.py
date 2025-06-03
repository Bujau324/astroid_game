import pygame
from constants import *
import circleshape
import player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # initialize screen for display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # new pygame.time.clock object
    clock = pygame.time.Clock()
    dt = 0
    # instantiate player object
    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)



    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        player1.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
