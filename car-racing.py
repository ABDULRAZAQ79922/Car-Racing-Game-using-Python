import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
CAR_WIDTH = 50
CAR_HEIGHT = 100
ENEMY_CAR_WIDTH = 50
ENEMY_CAR_HEIGHT = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Fancy Car Racing Game')

# Load images
car_image = pygame.image.load('car.jpeg')
enemy_car_image = pygame.image.load('enemy_car.jpeg')

# Function to display the car
def display_car(x, y):
    screen.blit(car_image, (x, y))

# Function to display enemy car
def display_enemy_car(x, y):
    screen.blit(enemy_car_image, (x, y))

# Main game loop
def game_loop():
    # Initial positions
    car_x = (SCREEN_WIDTH * 0.45)
    car_y = (SCREEN_HEIGHT * 0.8)
    car_x_change = 0

    enemy_car_start_x = random.randrange(0, SCREEN_WIDTH - ENEMY_CAR_WIDTH)
    enemy_car_start_y = -ENEMY_CAR_HEIGHT
    enemy_car_speed = 7

    clock = pygame.time.Clock()
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            
            # Key press events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change = -5
                if event.key == pygame.K_RIGHT:
                    car_x_change = 5
            
            # Key release events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_x_change = 0

        car_x += car_x_change

        screen.fill(WHITE)

        # Enemy car movement
        display_enemy_car(enemy_car_start_x, enemy_car_start_y)
        enemy_car_start_y += enemy_car_speed

        display_car(car_x, car_y)

        # Reset enemy car position after it moves out of screen
        if enemy_car_start_y > SCREEN_HEIGHT:
            enemy_car_start_y = -ENEMY_CAR_HEIGHT
            enemy_car_start_x = random.randrange(0, SCREEN_WIDTH - ENEMY_CAR_WIDTH)

        # Collision detection
        if car_y < enemy_car_start_y + ENEMY_CAR_HEIGHT:
            if car_x > enemy_car_start_x and car_x < enemy_car_start_x + ENEMY_CAR_WIDTH or car_x + CAR_WIDTH > enemy_car_start_x and car_x + CAR_WIDTH < enemy_car_start_x + ENEMY_CAR_WIDTH:
                crashed = True

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

game_loop()
