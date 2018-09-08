
class Agent:
    def __init__(self, cell=None, grid=None):
        self.cell = cell
        self.grid = grid

    def __setattr__(self, key, val):
        # if key == 'cell':
        #     oldcell = self.__dict__.get(key, None)
        #     if oldcell is not None:
        #         self.grid.agents.remove(self)
        #     if val is not None:
        #         self.grid.agents.remove(self)
        self.__dict__[key] = val

    def display(self):
        self.cell.display()