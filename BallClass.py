class Ball:
    def __init__(self, pos=(0, 0)):
        self.location= list(pos)
    
    def move(self, dx, dy):
        self.location[0] += dx
        self.location[1] += dy
