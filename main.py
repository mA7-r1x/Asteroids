import pygame
from constants import *

pygame.init()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user clicks the close button
                return  # Exit the game loop and thus the `main()` function
        
        screen.fill((0, 0, 0))  # Fill screen with black
        pygame.display.flip()   # Refresh the display

# Don't forget to call the main function to start your program!
main()


