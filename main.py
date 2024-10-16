import pygame
import sys

from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')

        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if player.colission(asteroid):
                sys.exit("Game over!")
            for bullet in shots:
                if asteroid.colission(bullet):
                    asteroid.kill()
                    bullet.kill()
                    asteroid.split(asteroids)

        dt_ms = clock.tick(60)
        dt = dt_ms / 1000
        pygame.display.flip()
if __name__ == "__main__":
    main()