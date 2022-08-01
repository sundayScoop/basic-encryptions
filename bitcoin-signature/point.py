from re import A
from polynomial import polynomial


class Point:
    def __init__(self, x=None, y=None, a=0, b=7, m=115792089237316195423570985008687907853269984665640564039457584007908834671663):
        self.x = x
        self.y = y
        self.a = a ## Quick hack
        self.b = b
        self.m = m
    
    def __add__(self, other):
        new_point = Point()
        if isinstance(other, Point):
            if other.x != self.x and other.y != self.y:
                slope = ((self.y - other.y) * pow(self.x - other.x, -1, self.m)) % self.m
                new_point.x = (pow(slope, 2) - self.x - other.x) % self.m
                new_point.y = (slope * (self.x - new_point.x) - self.y) % self.m
            else:
                slope = ((3*pow(self.x, 2) + self.a) * pow(2 * self.y, -1, self.m)) % self.m
                new_point.x = (pow(slope, 2) - (2 * self.x)) % self.m
                new_point.y = (slope * (self.x - new_point.x ) - self.y) % self.m
                
            return new_point
    
    def __mul__(self, multiplier: int):
        new_point = Point()
        new_point.x = self.x
        new_point.y = self.y

        multiplier = list(bin(multiplier)[3:])

        for x_a in multiplier:
            new_point = new_point + new_point  #2P
            if x_a == '1':
                new_point = new_point + self  #P + G
        return new_point
