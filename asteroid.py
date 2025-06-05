import pygame
from constants import *
import circleshape
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
       self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # random angle for two new asteroids to spawn
            random_angle = random.uniform(20, 50)
            # rotate upon random angle in opposite directions
            rotated1 = self.velocity.rotate(random_angle)
            rotated2 = self.velocity.rotate(-random_angle)
            # create two new asteroids with new radius
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            # update new asteroids velocity
            asteroid_a.velocity = rotated1 * 1.2
            asteroid_b.velocity = rotated2 * 1.2
