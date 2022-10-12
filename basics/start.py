import pygame
from sys import exit


pygame.init()
FPS = 60
screen = pygame.display.set_mode((800, 400)) # set display
pygame.display.set_caption("Hui") # название в окошке
clock = pygame.time.Clock() # to update game with tick
# default settings
default_settings = {"score": 0, "player_health": 100, "player_x": 100, "player_gravity": 1}

game_state = True
# to create font
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# to create surface
end_surface = pygame.Surface((800, 400))
end_surface.fill('black')

ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()
sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()

# player
player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(100, 300))

right_movement = False
left_movement = False

#snail
snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_rect = snail_surface.get_rect(midbottom=(600, 300))


while True:
    if game_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # so you can quit
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if player_rect.bottom == 300:
                        default_settings["player_gravity"] = -20
                if event.key == pygame.K_RIGHT:
                    right_movement = True
                if event.key == pygame.K_LEFT:
                    left_movement = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    right_movement = False
                if event.key == pygame.K_LEFT:
                    left_movement = False


            # working with mouse
            # if event.type == pygame.MOUSEMOTION:
            #     if player_rect.collidepoint(event.pos):
            #         player_rect.bottom -= 50
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     player_rect.bottom -= 50
            # if event.type == pygame.MOUSEBUTTONUP:
            #     player_rect.bottom += 50

        # draw all elements
        # update everything
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300)) # to draw surface
        # screen.blit(text_surface, (250, 250))  # to draw text


        # score
        score_surface = test_font.render(f"Score {default_settings['score']}", False, "Green")
        score_rect = score_surface.get_rect(midbottom=(380, 100))

        # drawings
        pygame.draw.rect(screen, "pink", score_rect)
        screen.blit(score_surface, score_rect)



        # player
        # player_health
        health_surface = test_font.render(f"HP: {default_settings['player_health']}", False, "red")
        health_rect = health_surface.get_rect(midbottom=(100, 100))
        screen.blit(health_surface, health_rect)
        pygame.draw.line(screen, 'red', (50, 110), (default_settings["player_health"] + 50, 110), 10)

        screen.blit(player_surface, player_rect)
        if player_rect.colliderect(snail_rect):
            snail_rect.left += 50
            default_settings["player_health"] -= 10
        default_settings["player_gravity"] += 1
        player_rect.y += default_settings["player_gravity"]
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        if right_movement:
            player_rect.x += 4
        if left_movement:
            player_rect.x -= 4


        #snail
        if snail_rect.left < 0:
            snail_rect.left = 800
        snail_rect.left -= 4
        screen.blit(snail_surface, snail_rect)


        # to work with mouse
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     player_rect.bottom -= 10

        if default_settings["player_health"] == 0:
            game_state = False
        pygame.display.update()
        clock.tick(FPS)



    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # so you can quit
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = True
                    snail_rect.x = 600
                    player_rect.x = 100
                    right_movement = False
                    left_movement = False
                    default_settings = {"score": 0, "player_health": 100, "player_gravity": 1}

        screen.fill('black')
        screen.blit(test_font.render("POTRACHENO", False, 'red'), (330, 200))
        pygame.display.update()
        clock.tick(FPS)

