import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 100
OPPONENT_WIDTH = 50
OPPONENT_HEIGHT = 100

# Colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)

# Set up the display
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Exciting Car Racing Game')

# Load images
player_car_img = pygame.image.load('car.jpeg')
opponent_car_img = pygame.image.load('enemy_car.jpeg')

# Function to display the player car
def show_player_car(x, y):
    window.blit(player_car_img, (x, y))

# Function to display opponent car
def show_opponent_car(x, y):
    window.blit(opponent_car_img, (x, y))

# Main game loop
def main_game_loop():
    # Initial positions
    player_x = (WINDOW_WIDTH * 0.45)
    player_y = (WINDOW_HEIGHT * 0.8)
    player_x_change = 0

    opponent_x = random.randrange(0, WINDOW_WIDTH - OPPONENT_WIDTH)
    opponent_y = -OPPONENT_HEIGHT
    opponent_speed = 7

    clock = pygame.time.Clock()
    game_over = False
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            # Key press events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -5
                if event.key == pygame.K_RIGHT:
                    player_x_change = 5
            
            # Key release events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

        player_x += player_x_change

        window.fill(COLOR_WHITE)

        # Opponent car movement
        show_opponent_car(opponent_x, opponent_y)
        opponent_y += opponent_speed

        show_player_car(player_x, player_y)

        # Reset opponent car position after it moves out of screen
        if opponent_y > WINDOW_HEIGHT:
            opponent_y = -OPPONENT_HEIGHT
            opponent_x = random.randrange(0, WINDOW_WIDTH - OPPONENT_WIDTH)
            score += 1

        # Collision detection
        if player_y < opponent_y + OPPONENT_HEIGHT:
            if (player_x > opponent_x and player_x < opponent_x + OPPONENT_WIDTH) or (player_x + PLAYER_WIDTH > opponent_x and player_x + PLAYER_WIDTH < opponent_x + OPPONENT_WIDTH):
                game_over = True

        # Display score
        font = pygame.font.SysFont(None, 55)
        score_text = font.render("Score: " + str(score), True, COLOR_BLACK)
        window.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

main_game_loop()
