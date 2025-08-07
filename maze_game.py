import pygame
import sys
from player import Player

class MazeGame:
    def __init__(self, image_path, start, goal, bad_points):
        pygame.init()
        self.screen = pygame.display.set_mode((398, 300))
        pygame.display.set_caption("Maze Game")

        self.maze_image = pygame.image.load(image_path).convert()
        self.screen.blit(self.maze_image, (0, 0))
        pygame.display.update()

        self.start = start
        self.goal = goal
        self.bad_points = bad_points
        self.player = Player(*start)
        self.clock = pygame.time.Clock()
        self.running = True

    def is_touching_wall(self, x, y):
        for dx in range(-self.player.radius, self.player.radius + 1):
            for dy in range(-self.player.radius, self.player.radius + 1):
                dist_sq = dx ** 2 + dy ** 2
                if dist_sq <= self.player.radius ** 2:
                    try:
                        pixel = self.maze_image.get_at((x + dx, y + dy))[:3]
                        if pixel == (0, 0, 0):
                            return True
                    except IndexError:
                        return True  # Вихід за межі
        return False

    def is_goal_reached(self):
        return abs(self.player.x - self.goal[0]) <= 5 and abs(self.player.y - self.goal[1]) <= 5

    def is_wrong_path(self, x, y):
        for bx, by in self.bad_points:
            if abs(x - bx) <= 5 and abs(y - by) <= 5:
                return True
        return False

    def is_back_move(self):
        return self.player.prev_pos == (self.player.x, self.player.y)

    def handle_move(self, dx, dy):
        new_x = self.player.x + dx * self.player.step
        new_y = self.player.y + dy * self.player.step

        if self.is_touching_wall(new_x, new_y):
            print("Шарік вдарився об стіну, гра завершена.")
            self.running = False
            return

        if self.player.prev_pos == (new_x, new_y):
            print("Шарік злякався і втік, гра завершена.")
            self.running = False
            return

        if self.is_wrong_path(new_x, new_y):
            print("Шарік заблукав, гра завершена.")
            self.running = False
            return

        self.player.move(dx, dy)

        if self.is_goal_reached():
            print("Вітаємо! Шарік пройшов лабіринт.")
            self.running = False
        else:
            print("Шарік знайшов правильний шлях.")

    def run(self):
        while self.running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.handle_move(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.handle_move(0, 1)
                    elif event.key == pygame.K_LEFT:
                        self.handle_move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.handle_move(1, 0)

            self.screen.blit(self.maze_image, (0, 0))
            self.player.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
        sys.exit()