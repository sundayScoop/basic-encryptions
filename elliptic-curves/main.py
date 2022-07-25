from polynomial import polynomial
from point import Point

p = polynomial(-1, 1)

point1 = Point(-1, p.getY(-1), p)
point2 = Point(-0.5, p.getY(-0.5), p)
point3 = point1 + point2

print("Point1: " + str(point1.y))

print(point3.x)
print(point3.y)