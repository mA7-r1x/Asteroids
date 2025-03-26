import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import *
from circleshape import CircleShape

pygame.init()

clock = pygame.time.Clock()
dt = 0
dt = clock.tick(60) / 1000

asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

Asteroid.containers = (asteroids, updatable, drawable)

Player.containers = (updatable, drawable)
AsteroidField.containers = (updatable)

asteroid_field = AsteroidField()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user clicks the close button
                return  # Exit the game loop and thus the `main()` function
        
        screen.fill((0, 0, 0))  # Fill screen with black

        updatable.update(dt)
        
        def update(self):
            # Update the position based on the velocity
            self.position += self.velocity


            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    print("Game over!")
                    sys.exit()  # Exit the program
         

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()   # Refresh the display

# Don't forget to call the main function to start your program!
main()


