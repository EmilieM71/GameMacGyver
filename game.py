# Importing modules
import pygame
from pygame.locals import *
from constants import *

# Pygame initialization
pygame.init()

# Loading resources :

# 1- Creating the Window
window = pygame.display.set_mode((cote_window, cote_window))

# 2- Window icon
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)

# 3- Window title
pygame.display.set_caption(title_window)

# Crop and resizing ans show wall image based on file
background_image = pygame.image.load(background_image).convert()
image_bg = background_image.subsurface(180, 240, 20, 20)
bg = pygame.transform.scale(image_bg, (450, 450))
window.blit(bg, (0, 0))

# Crop and resizing image hero
hero_source = pygame.image.load(hero_source).convert_alpha()
choice_hero = hero_source.subsurface(224, 0, 32, 32)
hero = pygame.transform.scale(choice_hero, (30, 30))
hero_position = hero.get_rect()

# Crop and resizing ans show wall image based on file
tiles_wall = pygame.image.load(wall_image).convert()
image_wall = tiles_wall.subsurface(280, 220, 20, 20)
wall = pygame.transform.scale(image_wall, (30, 30))

# Crop and resizing start image
start_image = pygame.image.load(start_image).convert()
image_start = start_image.subsurface(160, 20, 20, 20)
start = pygame.transform.scale(image_start, (30, 30))

# Crop, resizing and show arrival image
tiles_arrival = pygame.image.load(arrival_image).convert()
image_arrival = tiles_arrival.subsurface(220, 20, 20, 20)
arrival = pygame.transform.scale(image_arrival, (30, 30))


def generate_maze():
    path_list = []
    wall_list = []
    start_list = []
    arrival_list = []
    # Read the level file "Level1"
    with open("Level1", "r") as file:

        # Loop Speed Limitation
        pygame.time.Clock().tick(30)

        for x, line in enumerate(file):
            x *= size_sprite
            for y, c in enumerate(line):  # c for character
                y *= size_sprite
                if c == path_char:
                    path_list.append((x, y))  # Adding a member to list path
                elif c == start_char:
                    start_list.append((x, y))
                    path_list.append((x, y))
                    window.blit(start, (x, y))
                elif c == arrival_char:
                    arrival_list.append((x, y))
                    path_list.append((x, y))
                    window.blit(arrival, (x, y))
                elif c == wall_char:
                    wall_list.append((x, y))
                    print(wall_list)
                    for tuples in wall_list:
                        window.blit(wall, tuples)
                else:
                    break


# Variable that continues the loop if = 1, stops if = 0
Continue_games = 1

# Main loop
while Continue_games:

    # Loop Speed Limitation
    pygame.time.Clock().tick(30)

    window.blit(bg, (0, 0))
    generate_maze()

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

    window.blit(hero, hero_position)
    pygame.display.flip()
