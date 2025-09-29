import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
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
        random_angle = random.uniform(25, 50)
        vec1 = self.velocity.rotate(random_angle)
        vec2 = self.velocity.rotate(-random_angle)
        newradius = self.radius - ASTEROID_MIN_RADIUS
        newasteroid1 = Asteroid(self.position.x,self.position.y, newradius)
        newasteroid2 = Asteroid(self.position.x,self.position.y, newradius)
        newasteroid1.velocity = (vec1 * 1.2)
        newasteroid2.velocity = (vec2 * 1.2)