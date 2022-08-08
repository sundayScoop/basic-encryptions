import random
from re import M
from polynomial import Polynomial

class Ork:
    def __init__(self, x_list, my_x) -> None:
        self.x_list = x_list
        self.my_x = my_x
        self.polynomial: Polynomial = Polynomial(len(x_list))
        self.other_orks_y_list = []
    
    def getMyX(self):
        return self.my_x
    
    def set_other_orks_y_list(self, other_orks_y_list):
        self.other_orks_y_list = other_orks_y_list
    
    def generate_random_number(self):
        return random.randint(1, 10)

    def generate_random_polynomial(self):
        self.polynomial.generate_random_coefficients()
    
    def get_this_orks_ys_at_other_x_points(self):
        other_ys = {}
        for x_point in self.x_list:
            if x_point != self.my_x: ## Keep the Y at my_x secret
                other_ys[x_point] = self.polynomial.get_y_position(x_point)
        return other_ys
    
    def get_random_polynomial_point(self):
        result = 0
        for point in self.other_orks_y_list:
            result = result + point
        result = result + self.polynomial.get_y_position(self.my_x)
        return self.getMyX(), result

