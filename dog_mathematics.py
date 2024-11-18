from typing import Dict
from pygame import Surface
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animal mathematics")

# Make dog images
dogs = []
dog_height = 100
dog_width = 100
for index in range(1, 6):
    dog_image = pygame.image.load(f"dog{index}.jpg")
    dog_image = pygame.transform.scale(dog_image, (dog_width, dog_height))
    dogs.append(dog_image)

# Generate a random number of dogs (between 1 and 5)
num_dogs = random.randint(0, 5)

# Calculate the vertical space available
available_height = height - (num_dogs * dog_height) - 100

# Calculate the vertical gap between dogs
if num_dogs > 1:
    gap = available_height / (num_dogs - 1)
else:
    gap = 0

# Generate positions
dog_positions = []
for i in range(num_dogs):
    x = width
    y = i * (dog_height + gap)
    dog_positions.append((width // 2, y))

running = True
while running:
    # Quit if the user exits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    WHITE = (255, 255, 255)
    screen.fill(WHITE)

    # Draw the dogs
    for index in range(len(dog_positions)):
        screen.blit(dogs[index], dog_positions[index])

    # Create the text
    if num_dogs > 1:
        text = f"There are {num_dogs} dogs"
    else:
        text = "There is only 1 dog"
    font = pygame.font.Font(None, 36)
    BLACK = (0, 0, 0)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(width // 2, height - 50))

    # Draw the text
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()