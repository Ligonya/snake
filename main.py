import time
import pygame
import random

from directions import Direction
from snake import Snake

import config

def draw_game (window, snake, fruit):
    window.fill(config.background_color)

    if fruit is not None:
        pygame.draw.rect(
            window,
            config.fruit_color,
            pygame.Rect(fruit[0], fruit[1], config.fruit_width, config.fruit_height)
        )

    snake.draw(window)
    pygame.display.flip()

def start_game (window):
    snake = Snake()
    is_running = True
    fruit = None

    # Potentielle amélioration à faire => afficher le score.
    score = 0

    while is_running:
        snake.detect_collisions_with_self()

        for event in pygame.event.get():
            is_running = (
                not event.type == pygame.QUIT and
                not (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
            )

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and snake.direction != Direction.TOP:
                    snake.set_direction(Direction.BOTTOM)
                elif event.key == pygame.K_UP and snake.direction != Direction.BOTTOM:
                    snake.set_direction(Direction.TOP)
                elif event.key == pygame.K_LEFT and snake.direction != Direction.RIGHT:
                    snake.set_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT and snake.direction != Direction.LEFT:
                    snake.set_direction(Direction.RIGHT)

        # Détection collision avec le fruit.
        if snake.is_colliding_with_fruit(fruit):
            snake.eat()
            fruit = None
            score += 1

        """
            La méthode move va faire bouger le serpent en fonction
            de sa direction actuelle.
            Si celui-ci se retrouve, après son déplacement, en dehors
            de l'écran, alors la méthode return False et on reset à
            ce niveau la partie.
        """
        if not snake.move():
            snake = Snake()
            fruit = None
            score = 0

        if fruit is None:
            fruit = [
                random.randint(0, config.width - config.fruit_width),
                random.randint(0, config.height - config.fruit_height)
            ]

        time.sleep(config.refresh_rate)
        draw_game(window, snake, fruit)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption(config.title)
    pygame.display.set_icon(pygame.image.load('./assets/ico.png'))

    window = pygame.display.set_mode(config.dimensions)

    start_game(window)
    pygame.quit()
