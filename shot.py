from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        if hasattr(self.__class__, "containers"):
            for group in self.__class__.containers:
                group.add(self)


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width = 2)



    def update(self, dt):
        self.position += self.velocity * dt
