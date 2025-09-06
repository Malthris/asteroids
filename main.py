import pygame
import sys
from constants import *
from player import *
from asteroid import *
from circleshape import *
from asteroidfield import *



def main():
    
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    running = True
    while running: #gameloop
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        BLACK = (0, 0, 0)
        screen.fill(BLACK)

        #for updated in updatable:
        updatable.update(dt)
        for drawn in drawable:
            drawn.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game Over!")
                sys.exit()
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
