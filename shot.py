import pygame
from constants import *
import circleshape

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        self.SHOT_RADIUS = 5
        self.velocity = 0
        super().__init__(x, y, self.SHOT_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.SHOT_RADIUS, 2)
    
    def update(self, dt):
       self.position += (self.velocity * dt)
    
