# Importing modules
import pygame
from pygame.locals import *
from constants import *
from maze import Maze

# Pygame initialization
pygame.init()

# Loading resources :

# 1- Creating the Window
window_game = pygame.display.set_mode((cote_window, cote_window))

# 2- Window icon
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)

# 3- Window title
pygame.display.set_caption(title_window)

# Crop and resizing ans show wall image based on file
background_image = pygame.image.load(background_image).convert()
image_bg = background_image.subsurface(180, 240, 20, 20)
bg = pygame.transform.scale(image_bg, (460, 460))
window_game.blit(bg, (0, 0))

# Crop and resizing image hero
hero_source = pygame.image.load(hero_source).convert_alpha()
choice_hero = hero_source.subsurface(224, 0, 32, 32)
hero = pygame.transform.scale(choice_hero, (30, 30))
hero_position = hero.get_rect()

# Variable that continues the loop if = 1, stops if = 0
Continue_games = 1

# Main loop
while Continue_games:

    # Loop Speed Limitation
    pygame.time.Clock().tick(30)

    window_game.blit(bg, (0, 0))
    level = Maze("Level1")
    level.display(window_game)

    for event in pygame.event.get():  # We track the list of all the events received
        if event.type == QUIT:  # If one of these events is type QUIT
            Continue_games = 0  # We stop the loop
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                hero_position = hero_position.move(30, 0)
            elif event.key == K_LEFT:
                hero_position = hero_position.move(-30, 0)
            elif event.key == K_DOWN:
                hero_position = hero_position.move(0, 30)
            elif event.key == K_UP:
                hero_position = hero_position.move(0, -30)

    window_game.blit(hero, hero_position)
    pygame.display.flip()
