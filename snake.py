import pygame
from pygame.constants import NOEVENT
from directions import Direction
import config

class Snake():
    def __init__ (self):
        super(Snake, self).__init__()
        self.direction = Direction.RIGHT
        self.body = [[config.width / 2, config.height / 2]]

    def set_direction (self, direction):
        self.direction = direction

    def move (self):
        for index in range(len(self.body), 0, -1):
            current_position = self.body[index - 1]

            # horreur... mais j'ai pas trop d'autres solutions :/
            if index == 1:
                if self.direction == Direction.LEFT:
                    self.body[index - 1] = [current_position[0] - config.distance_travelled, current_position[1]]

                elif self.direction == Direction.RIGHT:
                    self.body[index - 1] = [current_position[0] + config.distance_travelled, current_position[1]]

                elif self.direction == Direction.TOP:
                    self.body[index - 1] = [current_position[0], current_position[1] - config.distance_travelled]

                else:
                    self.body[index - 1] = [current_position[0], current_position[1] + config.distance_travelled]
            else:
                self.body[index - 1] = self.body[index - 2]

        head = self.body[0]

        return (
            head[0] >= 0 and
            head[0] <= config.width - config.snake_width and
            head[1] >= 0 and
            head[1] <= config.height - config.snake_height
        )

    def eat (self):
        self.body.append([])

    def detect_collisions_with_self (self):
        # Le serpent n'est pas encore assez grand pour se mordre la queue.
        if len(self.body) < 3:
            return False

        head = self.body[0]
        for index in range(3, len(self.body)):
            snake_part = self.body[index]

            is_colliding = (
                snake_part[0] - config.snake_width < head[0] and
                snake_part[0] + config.snake_width > head[0] and
                snake_part[1] - config.snake_height < head[1] and
                snake_part[1] + config.snake_height > head[1]
            )

            if is_colliding:
                self.body = self.body[0:index]
                break

        return False

    def is_colliding_with_fruit (self, fruit):
        if fruit == None:
            return False

        head = self.body[0]

        return (
            head[0] >= fruit[0] - config.snake_width and
            head[0] <= fruit[0] + config.fruit_width and
            head[1] >= fruit[1] - config.snake_height and
            head[1] <= fruit[1] + config.fruit_height
        )

    def draw (self, window):
        for snake_part in self.body:
            pygame.draw.rect(
                window,
                config.snake_color,
                pygame.Rect(snake_part[0], snake_part[1], config.snake_width, config.snake_height)
            )
