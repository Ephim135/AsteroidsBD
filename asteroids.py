import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, asteroids):
        x, y, radius = self.position.x, self.position.y, self.radius
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        random_vector_meteor = self.velocity.rotate(random_angle)
        random_vector_meteor_negative = self.velocity.rotate(-random_angle)
        new_radius = radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(x, y, new_radius)
        asteroid2 = Asteroid(x, y, new_radius)
        asteroid1.velocity = random_vector_meteor * 1.2
        asteroid2.velocity = random_vector_meteor_negative * 1.2
        asteroids.add(asteroid1)
        asteroids.add(asteroid2)
