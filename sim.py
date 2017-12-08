from grid import Grid

class Sim(object):
    def __init__(self, grid):
        self.grid = grid

    def next_gen(self):
        for i in self.grid.grid:
            for j in i:
                print j.is_alive()
        return True

if __name__ == '__main__':
    grid = Grid(2, [(0, 0), (0, 1), (1,0)])
    sim = Sim(grid)
    sim.next_gen()
