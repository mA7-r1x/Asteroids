import pygame
from constants import *
from player import Player

pygame.init()

clock = pygame.time.Clock()
dt = 0
dt = clock.tick(60) / 1000

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
        
        player.update(dt)

        screen.fill((0, 0, 0))  # Fill screen with black
        player.draw(screen)
        pygame.display.flip()   # Refresh the display

# Don't forget to call the main function to start your program!
main()


