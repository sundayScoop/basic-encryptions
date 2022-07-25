from point import Point

class polynomial:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def getY(self, x_position):
        return pow(self.b + self.a*x_position + pow(x_position, 3), 0.5)
    
    def is_on_line(self, point: Point):
        print("-------")
        print(pow(self.b + self.a*point.x + pow(point.x, 3), 0.5))
        print(point.y)
        print("-------------")
        return (abs(pow(self.b + self.a*point.x + pow(point.x, 3), 0.5)) == abs(point.y)) ## You added abs here because there are 2 solutions