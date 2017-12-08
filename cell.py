class Cell(object):
    def __init__(self):
        self.alive = False

    def die(self):
        self.alive = False

    def reproduce(self):
        self.alive = True

    def is_alive(self):
        return self.alive
    
if __name__ == '__main__':
    cell = Cell()
