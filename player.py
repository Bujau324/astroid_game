import pygame
from constants import *
import circleshape
import shot


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # go left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # go right
            self.rotate(dt) 
        if keys[pygame.K_w]:
            # go up
            self.move(dt)
        if keys[pygame.K_s]:
            # go down
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            # shoot
            if self.timer < 0:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
            self.timer -= dt


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot1 = shot.Shot(self.position.x, self.position.y)
        shot1.velocity = pygame.Vector2(0,1).rotate(self.rotation)
        shot1.velocity *= PLAYER_SHOOT_SPEED
