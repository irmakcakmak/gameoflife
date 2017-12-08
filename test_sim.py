import unittest
from grid import Grid
from sim import Sim

class TestSim(unittest.TestCase):
    def test_cell_alive_next(self):
        grid = Grid(2, [(0, 0), (0, 1), (1,0)])
        sim = Sim(grid)
        sim.next_gen()
        self.assertTrue(sim.grid.grid[0][0].is_alive())
