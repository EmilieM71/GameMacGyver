from constants import size_sprite


class Position:
    """class for setting the position in x and y"""

    def __init__(self, x, y):
        self.position = (x, y)

    def __repr__(self):
        return str(self.position)

    # Hash d'un nombre
    def __hash__(self):
        return hash(self.position)

    # Comparateur d'égalité pour 2 positions
    def __eq__(self, pos):
        return self.position == pos.position

    # Méthode qui retourne une position
    def up(self):
        x, y = self.position
        return Position(x, y - size_sprite)

    def down(self):
        x, y = self.position
        return Position(x, y + size_sprite)

    def right(self):
        x, y = self.position
        return Position(x + size_sprite, y)

    def left(self):
        x, y = self.position
        return Position(x - size_sprite, y)


def main():

    p = Position(1, 14).right().left().up().down()
    print(p)


if __name__ == "__main__":
    main()
