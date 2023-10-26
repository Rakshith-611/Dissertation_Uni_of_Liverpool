import pygame
import sys
import nmm
import time
import random

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

BOARD = nmm.initial_state()
# BOARD =     [[nmm.USER, "$", "$", nmm.EMPTY, "$", "$", nmm.AI],
#             ["$", nmm.USER, "$", nmm.EMPTY, "$", nmm.AI, "$"],
#             ["$", "$", nmm.EMPTY, nmm.EMPTY, nmm.EMPTY, "$", "$"],
#             [nmm.EMPTY, nmm.EMPTY, nmm.EMPTY, "$", nmm.EMPTY, nmm.EMPTY, nmm.EMPTY],
#             ["$", "$", nmm.EMPTY, nmm.USER, nmm.EMPTY, "$", "$"],
#             ["$", nmm.AI, "$", nmm.EMPTY, "$", nmm.EMPTY, "$"],
#             [nmm.EMPTY, "$", "$", nmm.USER, "$", "$", nmm.AI]
#             ]
# Calculated intersection positions
intersections = [(130, 130), (300, 130), (470, 130),
                 (192, 192), (300, 192), (408, 192),
                 (250, 250), (300, 250), (352, 250),
                 (130, 300), (192, 300), (250, 300), (352, 300), (408, 300), (470, 300),
                 (250, 352), (300, 352), (350, 352),
                 (192, 408), (300, 408), (408, 408),
                 (130, 470), (300, 470), (470, 470)]

DIFFICULTY = None
PLAYER = 1

USER_PIECES = 9
AI_PIECES = 9
REMAINING_USER_PIECES = 0
REMAINING_AI_PIECES = 0

# activation for gameplay screen interactive elements
gameplay_active = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(wood)

    # get the ai depth (Landing Page)
    if DIFFICULTY is None:

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
                DIFFICULTY = nmm.BEGINNER
            elif intermediateButton.collidepoint(mouse):
                time.sleep(0.2)
                DIFFICULTY = nmm.INTERMEDIATE

    # Gameplay page
    else:

        gameplay_active = True
        positions = nmm.board_positions(board=BOARD)
        playable_positions = {position: [positions[position][0], positions[position][1]] 
                              for position in positions 
                              if positions[position][1] == nmm.EMPTY}
        
        # display the game board
        board_surface = pygame.image.load("Graphics/gameboard.jpg").convert_alpha()
        board_surface = pygame.transform.scale(board_surface, (400,400))
        board_rect = board_surface.get_rect(center = (300,300))
        screen.blit(board_surface, board_rect)


        # add playable positions
        tiles = {}
        for position, intersection in enumerate(intersections):
            intersection_rect = pygame.Rect(intersection[0]-14, intersection[1]-14, 28, 28)
            tiles[position + 1] = intersection_rect

            if positions[position+1][1] != nmm.EMPTY:
                if positions[position+1][1] == nmm.USER:
                    pygame.draw.circle(surface=screen, color=white, center=intersection, radius=14)
                elif positions[position+1][1] == nmm.AI:
                    pygame.draw.circle(surface=screen, color=black, center=intersection, radius=14)
            else:
                pygame.draw.circle(surface=screen, color=gold, center=intersection, radius=14)

        game_over = nmm.terminal(BOARD, USER_PIECES, AI_PIECES, REMAINING_USER_PIECES, REMAINING_AI_PIECES)


        # gameplay titles
        if game_over:
            winner = nmm.winner(BOARD, USER_PIECES, AI_PIECES, REMAINING_USER_PIECES, REMAINING_AI_PIECES)
            if winner is None:
                title = "Game Over: TIE."
            elif winner == nmm.USER:
                title = "Game Over: You WIN!"
            else:
                title = "Game Over: You lose :("

            againButton = pygame.Rect(200, 525, 200, 50)
            again = mediumFont.render("Play Again?", True, yellow)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, pecan, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    DIFFICULTY = None
                    PLAYER = 1
                    BOARD = nmm.initial_state()
        else:
            if PLAYER == nmm.USER:
                title = "Your turn."
            else:
                title = "Computer thinking..."

            user_pieces_text = smallFont.render("Unplayed", True, white)
            user_pieces_textRect = user_pieces_text.get_rect()
            user_pieces_textRect.center = (50, 150)
            screen.blit(user_pieces_text, user_pieces_textRect)
            user_pieces = largeFont.render(str(USER_PIECES), True, white)
            user_piecesRect = user_pieces.get_rect()
            user_piecesRect.center = (50, 200)
            screen.blit(user_pieces, user_piecesRect)

            ai_pieces_text = smallFont.render("Unplayed", True, black)
            ai_pieces_textRect = ai_pieces_text.get_rect()
            ai_pieces_textRect.center = (550, 150)
            screen.blit(ai_pieces_text, ai_pieces_textRect)
            ai_pieces = largeFont.render(str(AI_PIECES), True, black)
            ai_piecesRect = ai_pieces.get_rect()
            ai_piecesRect.center = (550, 200)
            screen.blit(ai_pieces, ai_piecesRect)

            r_user_pieces_text = smallFont.render("Remaining", True, white)
            r_user_pieces_textRect = r_user_pieces_text.get_rect()
            r_user_pieces_textRect.center = (50, 350)
            screen.blit(r_user_pieces_text, r_user_pieces_textRect)
            r_user_pieces = largeFont.render(str(REMAINING_USER_PIECES), True, white)
            r_user_piecesRect = r_user_pieces.get_rect()
            r_user_piecesRect.center = (50, 400)
            screen.blit(r_user_pieces, r_user_piecesRect)

            r_ai_pieces_text = smallFont.render("Remaining", True, black)
            r_ai_pieces_textRect = r_ai_pieces_text.get_rect()
            r_ai_pieces_textRect.center = (550, 350)
            screen.blit(r_ai_pieces_text, r_ai_pieces_textRect)
            r_ai_pieces = largeFont.render(str(REMAINING_AI_PIECES), True, black)
            r_ai_piecesRect = ai_pieces.get_rect()
            r_ai_piecesRect.center = (550, 400)
            screen.blit(r_ai_pieces, r_ai_piecesRect)
        
        title = largeFont.render(title, True, gold)
        titleRect = title.get_rect()
        titleRect.center = (300, 50)
        screen.blit(title, titleRect)


        # check for AI move
        if PLAYER == 2 and not game_over:
            # move = nmm.minimax(BOARD, DIFFICULTY)
            # print([value[0] for value in playable_positions.values()])
            move = random.choice([value[0] for value in playable_positions.values()])
            # print(move)
            BOARD, PLAYER = nmm.result(board=BOARD, action=move, player=PLAYER)
            if AI_PIECES > 0:
                AI_PIECES -= 1
                REMAINING_AI_PIECES += 1


        # check for user move
        click, _, _ = pygame.mouse.get_pressed()
        if click and PLAYER == 1 and not game_over:
            if USER_PIECES > 0:
                mouse = pygame.mouse.get_pos()
                for position in positions:
                    if (positions[position][1] == nmm.EMPTY and tiles[position].collidepoint(mouse)):
                        action = positions[position][0]
                        # print(f"Mouse clicked on position {position}")
                        BOARD, PLAYER = nmm.result(BOARD, action, PLAYER)
                        if USER_PIECES > 0:    
                            USER_PIECES -= 1
                            REMAINING_USER_PIECES += 1
            else:
                # REMAINING_USER_PIECES, _ = nmm.remaining_pieces(board=BOARD)
                # if REMAINING_USER_PIECES > 3:
                ...


    pygame.display.flip()