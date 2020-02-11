

class Buildings:
    def __init__(self, windows, doors):
        self.windows = windows
        self.doors = doors


class Terminal(Buildings):
    def __init__(self, windows, doors, lounges):
        super().__init__(windows,doors)
        self.lounges = lounges


class Runway(Buildings):
    def __init__(self, windows, doors, size):
        super().__init__(windows,doors)
        self.size = size

