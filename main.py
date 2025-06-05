import pygame
from constants import *
import circleshape
import player
import asteroid
import asteroidfield
import sys
import shot

def main():
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # set both groups as containers for player
    player.Player.containers = (updatable, drawable)
    # set astroids to respective container along with other groups
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    # set asteroidfield to updatable group
    asteroidfield.AsteroidField.containers = (updatable)
    # set shots to respective groups
    shot.Shot.containers = (shots, updatable, drawable)

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
    # instantiate asteroid field object
    asteroid_field1 = asteroidfield.AsteroidField()



    while (True):
        for event in pygame.event.get():
            # allow exit from window
            if event.type == pygame.QUIT:
                return
        # black window
        screen.fill("black")
        # 60 fps
        dt = clock.tick(60) / 1000
        # input
        updatable.update(dt)
        for thing_a in asteroids:
            if thing_a.collision_check(player1):
                print("Game over!")
                sys.exit()
        # render
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
