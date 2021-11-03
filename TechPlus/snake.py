import pygame
import random


### SETUP ###
pygame.init()

MAX_X = 600
MAX_Y = 400
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("My First Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("tahoma", 25)

### CONSTANTS ###
WHITE = (255, 255, 255)
GREEN = (150, 255, 160)
BLACK = (0, 0, 0)
RED = (255, 50, 50)

BLOCK_SIZE = 10

LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"

GAME_OVER_TEXT = font.render("Press C to restart or press Q to quit", True, BLACK)

### VARIABLE INITIALIZATION ###
game_over = False

snake_pos = list()
snake_maxlen = 1
x, y = (MAX_X / 2, MAX_Y / 2)  # center of screen
direction = RIGHT
x_delta, y_delta = (BLOCK_SIZE, 0)

food_x, food_y = (MAX_X / 2 - 20, MAX_Y / 2)

while True:

    ### EVENT HANDLING ###

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
                x_delta = -BLOCK_SIZE
                y_delta = 0
                break
                
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
                x_delta = BLOCK_SIZE
                y_delta = 0
                break

            elif event.key == pygame.K_UP and direction != DOWN:
                direction = UP
                x_delta = 0
                y_delta = -BLOCK_SIZE
                break

            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
                x_delta = 0
                y_delta = BLOCK_SIZE
                break

    ### SNAKE MOVEMENT ###

    x += x_delta
    y += y_delta
    snake_pos.insert(0, (x, y))  # insert to the front
    if len(snake_pos) > snake_maxlen:  # removes 1 tail block if needed
        snake_pos.pop()

    ### FOOD EVENT ###

    if (x, y) == (food_x, food_y):  # eats food
        snake_maxlen += 1
        # randomly generates new food
        food_x = round(random.randrange(0, MAX_X - BLOCK_SIZE), -1)
        food_y = round(random.randrange(0, MAX_Y - BLOCK_SIZE), -1)

    ### CHECK LOSE CONDITIONS ###

    if not (0 <= x < MAX_X and 0 <= y < MAX_Y):  # collision with border
        game_over = True
    if (x, y) in snake_pos[1:]:  # collision with own body
        game_over = True

    ### GAME OVER SCREEN ###

    while game_over:
        screen.fill(RED)
        screen.blit(GAME_OVER_TEXT, (MAX_X / 2 - 190, MAX_Y / 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # exits program
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:  # restart
                    # reset to original
                    game_over = False

                    snake_pos = list()
                    snake_maxlen = 1
                    x, y = (MAX_X / 2, MAX_Y / 2)  # center of screen
                    direction = RIGHT
                    x_delta, y_delta = (BLOCK_SIZE, 0)

                    food_x, food_y = (MAX_X / 2 - 20, MAX_Y / 2)

        clock.tick(15)  # 15 frames/updates per second

    ### GRAPHICS ###

    screen.fill(GREEN)
    pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))  # drawing food
    for block in snake_pos:  # drawing snake
        pygame.draw.rect(screen, BLACK, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.set_caption("My First Snake Game - Score: " + str(snake_maxlen-1))
    pygame.display.update()

    clock.tick(15)  # 15 frames/updates per second
