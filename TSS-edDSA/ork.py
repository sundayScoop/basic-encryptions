import hashlib
import random
from polynomial import Polynomial
from point import Point

class Ork:
    def __init__(self, x_list, my_x, G: Point, p: int) -> None:
        self.x_list = x_list
        self.my_x = my_x
        self.polynomial: Polynomial = Polynomial(len(x_list), p)
        self.other_orks_y_list = []
        self.my_y: int = None
        self.G = G
        self.randd = -1
        self.p = p
    
    def getMyX(self):
        return self.my_x
    
    def set_other_orks_y_list(self, other_orks_y_list):
        self.other_orks_y_list = other_orks_y_list
    
    def generate_random_point(self) -> Point:
        self.randd = random.randint(1, 35)
        return self.G * self.randd # G * r = Point(x,y)

    def generate_random_polynomial(self):
        self.polynomial.generate_random_coefficients()
    
    def get_this_orks_ys_at_other_x_points(self):
        other_ys = {}
        for x_point in self.x_list:
            if x_point != self.my_x: ## Keep the Y at my_x secret
                other_ys[x_point] = self.polynomial.get_y_position(x_point)
        return other_ys
    
    # Returns the coordiantes (this_ork.x, y) required to do lagrange interpolation of the CMK
    def get_random_polynomial_point(self):
        self.my_y = self.polynomial.get_y_position(self.my_x)
        result = 0
        for y_point in self.other_orks_y_list:
            result = result + y_point
        result = result + self.my_y
        return self.getMyX(), result

    # returns partial lagrange interpolation for one specific X (the X of this ork)
    # if you sum up all of the result values from each ork you will get y value of
    # WARNING WARNING WARNING. SHOULD ONLY BE CALLABLE FROM THE ORK <-----------------------------------------------------------
    def get_partial_key(self):
        #result = self.my_y
        result = self.get_random_polynomial_point()[1] # Y value
        for x in self.x_list:
            if x != self.my_x:
                result = result * x * pow(x - self.my_x, -1, self.p)
        return result % self.p
    
    def sign_message(self, msg_to_sign: str, r: Point):
        #hash_data = bytes(Gr)
        #hash_data += bytes(msg_to_sign.encode('utf-8'))

        #e = int(hashlib.sha256(hash_data).hexdigest(), 16)
        rx_bytes = r.x.to_bytes(32, 'little')             # Little endian!!!! edDSA encoding standard
        ry_bytes = r.y.to_bytes(32, 'little')
        msg_bytes = bytes(msg_to_sign)

        hash_data = rx_bytes
        hash_data += ry_bytes
        hash_data += msg_bytes

        e = int(hashlib.sha256(hash_data).hexdigest(), 16) # integer value of the 32 byte hash

        print("P_key: " + str(self.get_partial_key()))
        print("Rand: " + str(self.randd))

        return (self.randd - (self.get_partial_key()*e))

    def get_partial_pub_key(self):  # Returns G * partialK. Multiplied together will be G * k which is pub key
        return self.G * self.get_partial_key()   #isn't partial key a negative sometimes???