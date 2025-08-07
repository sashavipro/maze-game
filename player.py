import pygame

class Player:
    def __init__(self, x, y, radius=4, color=(255, 0, 0), step=4):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.step = step
        self.prev_pos = None  # Для перевірки "назад"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, dx, dy):
        self.prev_pos = (self.x, self.y)
        self.x += dx * self.step
        self.y += dy * self.step

    def current_position(self):
        return (self.x, self.y)