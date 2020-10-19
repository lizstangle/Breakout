################################################################################
# INSTRUCTIONS:
# Complete the TODOS below to add another "enemy" character. When the player 
# collides with the enemy, it should reset points to 0.
# 
# STRETCH CHALLENGES (complete if you've already finished the main challenge):
# 1. Add a "You Lose" screen that shows for 2 seconds if the player collides
#    with an enemy.
# 2. Create multiple enemies that can all fall at once.
################################################################################

import pygame
import random

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Make School Starter Game!')

################################################################################
# VARIABLES
################################################################################

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

CHARACTER_WIDTH = 40
CHARACTER_HEIGHT = 40

BALL_WIDTH = 10
BALL_HEIGHT = 10

PADDLE_WIDTH = 70
PADDLE_HEIGHT = 10

# Color constants 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Paddle Variables
paddle_x = 2
paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT * 1.25

paddle_x_velocity = 20

# Ball Variables
ball_x = 250
ball_y = 250

ball_x_velocity = 6 
ball_y_velocity = -6

# TODO: Add variables for the "enemy" character
#speed of paddle
# Other variables
velocity = 15
points = 0

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


################################################################################
# HELPER FUNCTIONS
################################################################################

def is_colliding(x1, y1, x2, y2, width, height):
    """Returns True if two rectangles are colliding, or False otherwise"""
    # If one rectangle is on left side of the other 
    if (x1 >= x2 + width) or (x2 >= x1 + width):
        return False
  
    # If one rectangle is above the other
    if (y1 >= y2 + height) or (y2 >= y1 + height):
        return False
  
    return True


def is_colliding2(ball_x_min, ball_x_max, ball_y_min, ball_y_max,
                  paddle_x_min, paddle_x_max, paddle_y_min, paddle_y_max):
    """Returns True if two rectangles are colliding, or False otherwise"""
    # If one rectangle is on left side of the other 
    if (ball_y_max >= paddle_y_min):
        return True
  
    # If one rectangle is above the other
    if (y1 >= y2 + height) or (y2 >= y1 + height):
        return False
  
    return True




def draw_text(text, color, font_size, x, y):
    font = pygame.font.SysFont(None, font_size)
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

################################################################################
# GAME LOOP
################################################################################

# Run until the user asks to quit
running = True
while running:
    # Advance the clock
    # pygame.time.delay(20)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update the paddle
    if keys[pygame.K_LEFT]:
        paddle_x -= velocity
    if keys[pygame.K_RIGHT]:
        paddle_x += velocity
    # if keys[pygame.K_UP]:
    #     paddle_y -= velocity
    # if keys[pygame.K_DOWN]:
    #     paddle_y += velocity

    # Update the ball
    ball_x += ball_x_velocity
    ball_y += ball_y_velocity


    # TODO: Update the enemy's y position based on its velocity

    # If ball goes off the screen, make it reverse direction to stay on screen
    # There are 4 limits and everytime it exceeds 1 limit it needs to flip opposite direction  
    if ball_y > SCREEN_HEIGHT: 
        ball_y_velocity = -ball_y_velocity

    if ball_x > SCREEN_HEIGHT:
        ball_x_velocity = -ball_x_velocity

    if ball_y < 0:
        ball_y_velocity = -ball_y_velocity

    if ball_x < 0: 
        ball_x_velocity = -ball_x_velocity   


    # If paddle collides with ball, reset it & increment points
    if is_colliding(paddle_x, paddle_y, ball_x, ball_y, CHARACTER_WIDTH, CHARACTER_HEIGHT):
        points += 1
        ball_y = 0
        ball_x = random.random() * (SCREEN_WIDTH - CHARACTER_WIDTH)

    # TODO: If paddle collides with enemy, reset it & set points to 0

    # Fill screen with white
    screen.fill(WHITE)

    # Draw the paddle as a blue rectangle
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    pygame.draw.rect(screen, RED, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the ball as a red square
    pygame.draw.rect(screen, RED, (ball_x, ball_y, BALL_WIDTH, BALL_HEIGHT))

    # TODO: Draw the enemy as a red square

    # Draw the points
    draw_text(text=f'Points: {points}', color=BLACK, font_size=24, x=20, y=20)

    # Update the game display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()