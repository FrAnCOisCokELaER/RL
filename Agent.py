
class Agent:
    def __init__(self, cell, grid):
        self.cell = cell
        self.grid = grid

    def __setattr__(self, key, val):
        if key == 'cell':
            old = self.__dict__.get(key, None)
            if old is not None:
                seld
            if val is not None:
                old.agents.append(self)
        self.__dict__[key] = val
