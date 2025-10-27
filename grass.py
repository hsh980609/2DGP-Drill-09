from pico2d import load_image


class Grass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(self.x, self.y)
        # self.image.draw(400, 30)

    def update(self):
        pass

