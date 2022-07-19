class Orc:
    def __init__(self, point, t, n, other_secret_number) -> None:
        self.point = point
        self.t = t
        self.n = n
        self.other_secret_number = other_secret_number

    def get_share(self):
        return [self.point[0], self.point[1] + self.other_secret_number]