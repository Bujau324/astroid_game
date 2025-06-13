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

    # initializing constructor
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


    # GUI stuff
    # defining a font
    smallfont = pygame.font.SysFont("Corbel", 35)

    # rendering a text written in this font
    quit_text = smallfont.render("quit", True, WHITE_COLOR)
    retry_text = smallfont.render("retry", True, WHITE_COLOR)

    

    # game loop
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
        # ship to asteroid collision check
        for aster in asteroids:
            if aster.collision_check(player1):
                print("Game over!")
                # pause game
                is_paused = True
                while is_paused:
                    # Play again??? or Quit??
                    # Quit section
                    # stores the (x,y) coordinates into the variable as a tuple
                    mouse = pygame.mouse.get_pos()

                    # if mouse is hovered on a button it changes to the lighter shade
                    if SCREEN_WIDTH / 2 <= mouse[0] <= SCREEN_WIDTH / 2 + 140 and SCREEN_HEIGHT / 2 <= mouse[1] <= SCREEN_HEIGHT / 2 + 40:
                        pygame.draw.rect(screen, LIGHT_SHADE, [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 140, 40])
                    else:
                        # draw normal darker shade button
                        pygame.draw.rect(screen, DARK_SHADE, [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 140, 40])

                    # superimposing the text onto our button
                    screen.blit(quit_text, (SCREEN_WIDTH / 2 + 50, SCREEN_HEIGHT / 2))

                    # retry button here in different position.
                    # if mouse is hovered on a button it changes to the lighter shade
                    if SCREEN_WIDTH / 3 <= mouse[0] <= SCREEN_WIDTH / 3 + 140 and SCREEN_HEIGHT / 3 <= mouse[1] <= SCREEN_HEIGHT / 3 + 40:
                        pygame.draw.rect(screen, LIGHT_SHADE, [SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3, 140, 40])
                    else:
                        # draw normal darker shade button
                        pygame.draw.rect(screen, DARK_SHADE, [SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3, 140, 40])

                    # superimposing the text onto our button
                    screen.blit(retry_text, (SCREEN_WIDTH / 3 + 50, SCREEN_HEIGHT / 3))

                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            is_paused = False
                            pygame.quit()
                        
                        # check if a mouse is clicked
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            # if the mouse is clicked on the
                            # Quit button the game is terminated
                            if SCREEN_WIDTH / 2 <= mouse[0] <= SCREEN_WIDTH / 2 + 140 and SCREEN_HEIGHT / 2 <= mouse[1] <= SCREEN_HEIGHT / 2 + 40:
                                pygame.quit()
                                is_paused = False
                            elif SCREEN_WIDTH / 3 <= mouse[0] <= SCREEN_WIDTH / 3 + 140 and SCREEN_HEIGHT / 3 <= mouse[1] <= SCREEN_HEIGHT / 3 + 40:
                                is_paused = False
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
