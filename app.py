import pygame
import sys
import nmm
import time

pygame.init()
size = width, height = 600, 600

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
wood = (97, 54, 19)
yellow = (255, 215, 0)
gold = (218, 165, 32)
pecan = (72, 38, 13)

# font size
smallFont = pygame.font.Font("OpenSans-Regular.ttf", 20)
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)

screen = pygame.display.set_mode(size)

board = nmm.initial_state()
# Calculated intersection positions
intersections = [(130, 130), (300, 130), (470, 130),
                 (192, 192), (300, 192), (408, 192),
                 (250, 250), (300, 250), (352, 250),
                 (130, 300), (192, 300), (250, 300), (352, 300), (408, 300), (470, 300),
                 (250, 352), (300, 352), (350, 352),
                 (192, 408), (300, 408), (408, 408),
                 (130, 470), (300, 470), (470, 470)]

difficulty = None
player = 1

# activation for gameplay screen interactive elements
gameplay_active = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # if gameplay_active and event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_x, mouse_y = pygame.mouse.get_pos()

        #     for i, intersection in enumerate(intersections):
        #         intersection_rect = pygame.Rect(intersection[0]-14, intersection[1]-14, 28, 28)  # Create Rect around intersection
        #         if intersection_rect.collidepoint(mouse_x, mouse_y):
        #             print(f"Mouse clicked on intersection {i+1}")

    screen.fill(wood)

    # get the ai depth (Landing Page)
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
        # button_y = ...

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

        # check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if beginnerButton.collidepoint(mouse):
                time.sleep(0.2)
                difficulty = nmm.BEGINNER
            elif intermediateButton.collidepoint(mouse):
                time.sleep(0.2)
                difficulty = nmm.INTERMEDIATE

    # Gameplay page
    else:

        gameplay_active = True
        
        # display the game board
        board_surface = pygame.image.load("Graphics/gameboard.jpg").convert_alpha()
        board_surface = pygame.transform.scale(board_surface, (400,400))
        board_rect = board_surface.get_rect(center = (300,300))
        screen.blit(board_surface, board_rect)

        # add playable positions
        # for intersection in intersections:
        #     pygame.draw.circle(surface=screen, color=gold, center=intersection, radius=14)
        for intersection in intersections:
            pygame.draw.circle(surface=screen, color=gold, center=intersection, radius=14)

        game_over = nmm.terminal(board=board)

        # if gameplay_active and event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_x, mouse_y = pygame.mouse.get_pos()

        #     for i, intersection in enumerate(intersections):
        #         intersection_rect = pygame.Rect(intersection[0]-14, intersection[1]-14, 28, 28)  # Create Rect around intersection
        #         if intersection_rect.collidepoint(mouse_x, mouse_y):
        #             print(f"Mouse clicked on intersection {i+1}")

        # add user input
        click, _, _ = pygame.mouse.get_pressed()
        if click and player == 1:# and not game_over:
            mouse = pygame.mouse.get_pos()
            for i, intersection in enumerate(intersections):
                intersection_rect = pygame.Rect(intersection[0]-14, intersection[1]-14, 28, 28)
                if intersection_rect.collidepoint(mouse):
                    print(f"Mouse clicked on intersection {i+1}")
                    move = i+1

    pygame.display.flip()