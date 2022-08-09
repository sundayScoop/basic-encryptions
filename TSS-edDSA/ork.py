import hashlib
import random
from polynomial import Polynomial
from point import Point

class Ork:
    def __init__(self, x_list, my_x, g) -> None:
        self.x_list = x_list
        self.my_x = my_x
        self.polynomial: Polynomial = Polynomial(len(x_list))
        self.other_orks_y_list = []
        self.my_y: int = None
        self.g = g
        self.randd = -1
    
    def getMyX(self):
        return self.my_x
    
    def set_other_orks_y_list(self, other_orks_y_list):
        self.other_orks_y_list = other_orks_y_list
    
    def generate_random_number(self):
        self.randd = random.randint(30, 35)
        return pow(self.g, self.randd)    # G^r

    def generate_random_polynomial(self):
        self.polynomial.generate_random_coefficients()
    
    def get_this_orks_ys_at_other_x_points(self):
        other_ys = {}
        for x_point in self.x_list:
            if x_point != self.my_x: ## Keep the Y at my_x secret
                other_ys[x_point] = self.polynomial.get_y_position(x_point)
        return other_ys
    
    def get_random_polynomial_point(self):
        self.my_y = self.polynomial.get_y_position(self.my_x)
        result = 0
        for point in self.other_orks_y_list:
            result = result + point
        result = result + self.my_y
        return self.getMyX(), result

    # returns partial lagrange interpolation for one specific X (the X of this ork)
    # if you sum up all of the result values from each ork you will get the secret
    def get_partial_key(self):
        result = self.my_y
        for x in self.x_list:
            if x != self.my_x:
                result = result * (x / (x - self.my_x))
        return result
    
    def sign_message(self, msg_to_sign: str, Gr: int):
        #hash_data = bytes(Gr)
        #hash_data += bytes(msg_to_sign.encode('utf-8'))

        #e = int(hashlib.sha256(hash_data).hexdigest(), 16)
        e = int('1', 16)

        print("P_key: " + str(self.get_partial_key()))
        print("Rand: " + str(self.randd))

        return (self.randd - (self.get_partial_key()*e))

    def get_partial_pub_key(self):  # Returns G^partialK. Multiplied together will be G^k which is pub key
        return pow(self.g, self.get_partial_key())