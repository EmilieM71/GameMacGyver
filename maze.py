from constants import (size_sprite, pathchar, startchar, arrivalchar, wallchar,
                       wall_image, start_image, arrival_image, cote_window)
from position import Position
import pygame


class Maze:
    """Class that generates and displays the maze characterised by a file, here "Level1" """

    def __init__(self, filename):  # Notre méthode constructeur
        """définition de l'attribut filename"""
        self.filename = filename
        self.window = pygame.display.set_mode((cote_window, cote_window))

        self._path = []
        self.start_list = []
        self._arrival = []
        self._wall = []

        self.structure_maze = self.load_maze_from_file()

    def is_path_position(self, position):
        return position in self._path

    def load_maze_from_file(self):
        """function that generates the map of the maze"""

        with open(self.filename, "r") as file:
            self.structure_maze = []
            for x, line in enumerate(file):
                x *= size_sprite
                line_maze = []
                for y, c in enumerate(line):  # c for character
                    y *= size_sprite
                    line_maze.append(c)
                    if c == pathchar:
                        self._path.append(Position(x, y))  # Adding a member to list path
                    elif c == startchar:
                        self.start_list.append(Position(x, y))
                        self._path.append(Position(x, y))
                    elif c == arrivalchar:
                        self._arrival.append(Position(x, y))
                        self._path.append(Position(x, y))
                    elif c == wallchar:
                        self._wall.append(Position(x, y))
                self.structure_maze.append(line_maze)
        return self.structure_maze

    def display(self, window_name):
        """function that displays the map of the maze"""

        # Crop and resizing start image
        tiles_start = pygame.image.load(start_image).convert()
        image_start = tiles_start.subsurface(160, 20, 20, 20)
        start = pygame.transform.scale(image_start, (30, 30))

        # Crop, resizing and show arrival image
        tiles_arrival = pygame.image.load(arrival_image).convert()
        image_arrival = tiles_arrival.subsurface(220, 20, 20, 20)
        arrival = pygame.transform.scale(image_arrival, (30, 30))

        # Crop and resizing ans show wall image based on file
        tiles_wall = pygame.image.load(wall_image).convert()
        image_wall = tiles_wall.subsurface(280, 220, 20, 20)
        wall = pygame.transform.scale(image_wall, (30, 30))

        num_line = 0
        for line in self.structure_maze:
            num_case = 0
            for letter in line:
                x = num_case * size_sprite
                y = num_line * size_sprite
                if letter == wallchar:
                    window_name.blit(wall, (x, y))
                elif letter == arrivalchar:
                    window_name.blit(arrival, (x, y))
                elif letter == startchar:
                    window_name.blit(start, (x, y))
                num_case += 1
            num_line += 1


def main():
    level = Maze("Level1")
    print(level)


if __name__ == "__main__":
    main()
