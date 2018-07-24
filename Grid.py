import random
from Cell import Cell
from Agent import Agent

class Grid:
    def __init__(self, width=None, height=None, filename=None, adjacency=8):
        self.width = None
        self.height = None
        self.cells = None
        self.agents = []

    def restartGrid(self, filename=None):
        #Set  up cells onto grid
        if filename is not None:
            data = open(filename).readlines()
            if self.height is None:
                self.height=len(data)
            if self.width is None:
                self.width=max([len(x.rstrip()) for x in data])
        else:
            raise RuntimeError('this is the error message')
        self.cells = tuple([[Cell(x,y,data[y][x],self) for x in range(self.width)] for y in range(self.height)])

        #init agent
        self.agents=[]
        #reinit iteration
        self.iteration = 0

    def Display(self):
        print('width is', self.width)
        print('height is', self.height)
        print( [[self.cells[y][x].display() for x in range(self.width)] for y in range(self.height)])

    def generateOffsets(self):
        if self.adjacency ==8:
            res = ( (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
        else:
            raise RuntimeError('only 8 neighbours adjacency is supported')

        return res

    def addAgent(self, agent, x=None, y=None, cell=None):
        self.agents.append(agent)
        if cell is not None:
            x = cell.x
            y = cell.y
        if x is None:
            x = random.randrange(self.width)
        if y is None:
            y = random.randrange(self.height)
        agent.cell = self.cells[y][x]



if __name__ == '__main__':
    mygrid = Grid()
    mygrid.restartGrid('map.txt')
    mygrid.Display()


    # def load(self, f):
    #     if not hasattr(self.Cell, 'load'):
    #         return
    #     if isinstance(f, type('')):
    #         f = file(f)
    #     lines = f.readlines()
    #     lines = [x.rstrip() for x in lines]
    #     fh = len(lines)
    #     fw = max([len(x) for x in lines])
    #     if fh > self.height:
    #         fh = self.height
    #         starty = 0
    #     else:
    #         starty = (self.height - fh) / 2
    #     if fw > self.width:
    #         fw = self.width
    #         startx = 0
    #     else:
    #         startx = (self.width - fw) / 2
    #
    #     self.reset()
    #     for j in range(fh):
    #         line = lines[j]
    #         for i in range(min(fw, len(line))):
    #             self.grid[starty + j][startx + i].load(line[i])
