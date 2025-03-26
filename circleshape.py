import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        print(f"DEBUG: Player Position: {self.position}, Asteroid Position: {other.position}")
        print(f"DEBUG: Distance: {distance}, Radii Sum: {self.radius + other.radius}")
        print(f"DEBUG: Is Colliding: {distance <= self.radius + other.radius}")           
        
        return distance <= self.radius + other.radius
    
