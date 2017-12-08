from cell import Cell

class Grid(object):
    def __init__(self, size, initial):
        self.grid = [[Cell() for j in range(size)] for i in range(size)]
        for i in initial:
            self.grid[i[0]][i[1]].reproduce()

if __name__ == '__main__':
    grid = Grid(5, [(2,3)])
