import pygame
import sys
import nmm

pygame.init()
size = width, height = 600, 600

# Colours
black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

board = nmm.initial_state()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()