from pico2d import load_image

# 생성할때 x,y값을 입력받아서 생성하고 그것을 기반으로 draw합니다.
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

