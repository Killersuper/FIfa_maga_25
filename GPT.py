# import pygame as pg

# # Инициализация Pygame
# pg.init()

# # Определение параметров окна
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 400
# FPS = 60

# # Определение цветов
# WHITE = (255, 255, 255)

# # Создание окна игры
# window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pg.display.set_caption("Футбол")

# clock = pg.time.Clock()

# running = True
# while running:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             running = False

#     # Отображение заднего фона
#     window.fill(WHITE)

#     # Обновление экрана
#     pg.display.update()
#     clock.tick(FPS)

# # Завершение игры
# pg.quit()



import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 800, 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Футбол")

# Функция для отрисовки поля
def draw_field():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (50, 50, WIDTH - 100, HEIGHT - 100), 2)
    pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), 70, 2)
    pygame.draw.line(screen, BLACK, (WIDTH // 2, 50), (WIDTH // 2, HEIGHT - 50), 2)
    pygame.display.update()

# Функция для отрисовки мяча
def draw_ball(ball_x, ball_y):
    pygame.draw.circle(screen, BLACK, (ball_x, ball_y), 10)
    pygame.display.update()

# Главный цикл игры
def main():
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_speed_x = random.randint(2, 4)
    ball_speed_y = random.randint(2, 4)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            ball_y -= 5
        if keys[pygame.K_DOWN]:
            ball_y += 5

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_x < 60 or ball_x > WIDTH - 60:
            ball_speed_x = -ball_speed_x

        if ball_y < 60 or ball_y > HEIGHT - 60:
            ball_speed_y = -ball_speed_y

        draw_field()
        draw_ball(ball_x, ball_y)

        pygame.time.delay(30)

# if name == "__main__":
#     main()