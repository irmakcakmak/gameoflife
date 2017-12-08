import unittest

from cell import Cell

class TestCell(unittest.TestCase):

    def test_die(self):
        cell = Cell()
        cell.alive = True
        cell.die()
        self.assertFalse(cell.alive)

    def test_reproduce(self):
        cell = Cell()
        cell.alive = False
        cell.reproduce()
        self.assertTrue(cell.alive)

    def test_is_alive(self):
        cell = Cell()
        cell.alive = True
        self.assertTrue(cell.is_alive())

    def test_is_not_alive(self):
        cell = Cell()
        cell.alive = False
        self.assertFalse(cell.is_alive())


if __name__ == '__main__':
    unittest.main()
