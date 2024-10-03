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

# List the dogs
dogs = []
for index in range(1, 6):
    dog_image = pygame.image.load(f"dog{index}.jpg")  # Make sure you have a dog.png file in the same directory
    dog_image = pygame.transform.scale(dog_image, (100, 100))  # Resize the image
    dogs.append(dog_image)

# Generate a random number of dogs (between 1 and 5)
num_dogs = random.randint(1, 5)

# Create a list of random positions for the dogs
dog_positions = [(random.randint(0, width - 100), random.randint(0, height - 200)) for dog in range(num_dogs)]

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
    text = f"There are {num_dogs} dogs"
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