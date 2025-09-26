import pygame
import random
from circleshape import *
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.split_angle = random.uniform(20, 50)
        angle_pos = self.velocity.rotate(self.split_angle)
        angle_neg = self.velocity.rotate(-self.split_angle)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid.velocity = angle_pos * 1.2
        
        asteroid = Asteroid(self.position.x, self.position.y, self.new_radius)
        asteroid.velocity.rotate(-self.split_angle)
        asteroid.velocity = angle_neg * 1.2