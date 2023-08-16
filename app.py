import pygame
import sys
import nmm

pygame.init()
size = width, height = 600, 600

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
wood = (133, 94, 66)
gold = (255, 215, 0)

# font size
smallFont = pygame.font.Font("OpenSans-Regular.ttf", 20)
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)

screen = pygame.display.set_mode(size)

board = nmm.initial_state()
difficulty = None

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(wood)

    # get the ai depth
    if difficulty is None:

        # display title
        title = largeFont.render("Nine Men's Morris", True, gold)
        titleRect = title.get_rect()
        titleRect.center = ((width/2), 100)
        screen.blit(title, titleRect)

        # display subtext
        text = smallFont.render("Select difficulty", True, gold)
        textRect = text.get_rect()
        textRect.center = [(width/2), 250]
        screen.blit(text, textRect)

    else:
        ...

    pygame.display.flip()