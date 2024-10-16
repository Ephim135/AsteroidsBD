import pygame

from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.SHOT_RADIUS = 5

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    