class Position:
    """Classe permettant de définir la position en x et en y"""

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
        return Position(x, y - 1)

    def down(self):
        x, y = self.position
        return Position(x, y + 1)

    def right(self):
        x, y = self.position
        return Position(x + 1, y)

    def left(self):
        x, y = self.position
        return Position(x - 1, y)


def main():

    p = Position(1, 14).right().left().up().down()
    print(p)


if __name__ == "__main__":
    main()