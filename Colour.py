class Colour(object):
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def get(self):
        return (self.R, self.G, self.B)
