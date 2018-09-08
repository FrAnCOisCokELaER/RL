import random
import os

#tuple
neighbourSynonyms = ('neighbours')

class Universe:

    def __init__(self,
                 width=None,
                 height=None,
                 directions=8,
                 filename=None):

        self.directions = directions

        #init map
        if filename is not None:
            self.load(filename)

        #should be in load method
        if filename is not None:
            data = open(filename).readlines()
            if height is None:
                self.height=len(data)
            if width is None:
                self.width=max([len(x.rstrip()) for x in data])
        if width is None:
            width=20
        if height is None:
            height=20
        self.height=height
        self.width=width

        self.cell = Cell()
        #need to create/init the grid cells the grid


    class Cell:
        def __init__(self):

        #get neighbours cells according to a given adjacency
        def __getattr__(self, neighbours):
            self.__dict__[neighbours] = ([])

    def reset(self):
        pass

    def getPointInDirection(self, x, y, dir):
        if self.directions == 8:
            dx,dy = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)][dir]
        elif self.directions == 4:
            dx, dy = [(0, -1), (1, 0), (0, 1), (-1, 0)][dir]

        xp = x + dx
        yp = y + dy

        if xp<0:
            xp+=self.width
        if yp<0:
            yp+=self.height
        if xp>=self.width
            xp-= self.width
        if yp>=self.height:
            yp-=self.height

        return(xp,yp)