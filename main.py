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


    # play again?
    retry = "Y"
    while (retry.upper() == "Y"):
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
        # ship to asteroid collision check
        for aster in asteroids:
            if aster.collision_check(player1):
                print("Game over!")
                # Play again???
                retry = input("Retry? Y/N: ")
                if retry.upper() == "Y":
                    # Reset player to center
                    player1.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    player1.velocity = pygame.Vector2(0,0)

                    # Reset player rotation
                    player1.rotation = 0

                    # Clear all existing game objects
                    for astero in asteroids.copy():
                        astero.kill()
                    for sho in shots.copy():
                        sho.kill()
                    
                    # Reset asteroid field spawn timer
                    asteroid_field1.spawn_timer = -5
                    
                else:
                    sys.exit()
            for shott in shots:
                if shott.collision_check(aster):
                    aster.split()
                    shott.kill()

        # render
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
