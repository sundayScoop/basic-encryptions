class Orc:
    def __init__(self, point, t, n, random_polynomial_y_position) -> None:
        self.point = point
        self.t = t
        self.n = n
        self.random_polynomial_y_position = random_polynomial_y_position

    def get_share(self):
        return [self.point[0], self.point[1] + self.random_polynomial_y_position]