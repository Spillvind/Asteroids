import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width = 2)
    
    def check_collision(self, CircleShape):

        distance_vector = self.position - CircleShape.position
        distance = self.position.distance_to(CircleShape.position)
        minimal_distance = self.radius + CircleShape.radius
        if distance <= minimal_distance:
            return True
        else:
            return False
        

        

    def update(self, dt):
        # sub-classes must override
        pass