import pygame
import sys
import nmm

pygame.init()
size = width, height = 600, 600

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
wood = (97, 54, 19)
yellow = (255, 215, 0)
gold = (218,165,32)
pecan = (72, 38, 13)

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
        textRect.center = [(width/2), 200]
        screen.blit(text, textRect)

        # button dimensions and centering
        buttonWidth = width / 2
        button_height = 50
        button_x = (width - buttonWidth) / 2

        # draw buttons
        beginnerButton = pygame.Rect(button_x, 300, buttonWidth, button_height)
        playBeginner = mediumFont.render("BEGINNER", True, yellow)
        playBeginnerRect = playBeginner.get_rect()
        playBeginnerRect.center = beginnerButton.center
        pygame.draw.rect(screen, pecan, beginnerButton)
        screen.blit(playBeginner, playBeginnerRect)

        intermediateButton = pygame.Rect(button_x, 400, buttonWidth, button_height)
        playIntermediate = mediumFont.render("INTERMEDIATE", True, yellow)
        playIntermediateRect = playIntermediate.get_rect()
        playIntermediateRect.center = intermediateButton.center
        pygame.draw.rect(screen, pecan, intermediateButton)
        screen.blit(playIntermediate, playIntermediateRect)

    else:
        ...

    pygame.display.flip()