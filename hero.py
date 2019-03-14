class Hero:

    def __init__(self, map):
        self.map = map
        self.position = self.map.start

    def move(self, direction):
        """Function that allows you to move the hero"""
        new_position = getattr(self.position, direction)()  # getattr(attribute ,function_name)(arguments)
        if new_position in self.map:
            self.position = new_position
