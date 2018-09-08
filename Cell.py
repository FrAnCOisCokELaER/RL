

class Cell:
    def __getattr__(self, neighbours):
        def circularshift(coord, width):
            if coord<0:
                coord+=width
            if coord>=width:
                coord-=width
            return coord

        #circular neighbours shifts
        self.__dict__['neighbours'] = tuple([self.grid.cells[circularshift(self.y+y, self.grid.height)]
                                             [circularshift(self.x+x, self.grid.width)]
                                             for (x, y) in self.grid.generateOffsets()])

    def __init__(self, x, y, value, grid):
        self.x = x
        self.y = y
        self.value = value
        self.grid = grid

    def display(self):
        print(self.y, self.x, self.value)
