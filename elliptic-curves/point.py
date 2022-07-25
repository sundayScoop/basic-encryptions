


class Point:
    def __init__(self, x=None, y=None, curve=None):
        self.x = x
        self.y = y
        self.curve = curve
    
    def __add__(self, other):
        new_point = Point()
        if isinstance(other, Point):
            if other != self:
                slope = (self.y - other.y)/(self.x - other.x)
                print("Slope: " + str(slope))
                new_point.x = pow(slope, 2) - (self.x + other.x)
                new_point.y = slope * (self.x - new_point.x) - self.y
            else:
                slope = (3*pow(self.x, 2) + self.curve.a) / (2 * self.y)
                print(slope)
                new_point.x = pow(slope, 2) - (2 * self.x)
                new_point.y = - self.y - slope * (new_point.x - self.x) 
                
            return new_point
    
    def my_add(self, other):
        new_point = Point()
        if isinstance(other, Point):
            if other == self:
                slope = (3*pow(self.x, 2) + self.curve.a) / (2 * self.y)
                tangent_c = self.y - (slope * self.x)
                pass
    
    def __mul__(self, other):
        new_point = Point()
        if isinstance(other, int):
            new_point = self
            for i in range(other):
                new_point = new_point + self
            return new_point