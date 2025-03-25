from asteroid import Asteroid
from circleshape import CircleShape
import pygame

# Initialize game groups
asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

# Link the Asteroid class to the groups
Asteroid.containers = (asteroids, updatable, drawable)

# Test making a single asteroid
test_asteroid = Asteroid(100, 100, 20)

# Print results
print(test_asteroid in asteroids)  # Should print `True`
print(test_asteroid in drawable)  