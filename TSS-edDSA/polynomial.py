import random

class Polynomial:
    def __init__(self, threshold, p) -> None:
        self.coefficent_list = []
        self.threshold = threshold
        self.p = p

    def get_y_position(self, x_position):
        y_position = self.coefficent_list[0] # y_intercept
        exponent_count = 1 # e.g. x^1 . y_position above would be x^0 (1), so just the y_interecept (first item) 

        for coefficient in self.coefficent_list[1:]: # [1:] because [0] has already been included in calc. above
            y_position = y_position + coefficient*pow(x_position, exponent_count)  # Change + to +/- option depending on coefficient
            exponent_count+=1
            

        return y_position % self.p
    
    def generate_random_coefficients(self):
        for i in range(self.threshold):
            self.coefficent_list.append(random.randint(1, 100))
        #print('y = {0} + {1}x +{2}x^(2) + {3}x^(3) + {4}x^(4) + {5}x^(5) + {6}x^(6) + {7}x^(7) + {8}x^(8) + {9}x^(9) + {10}x^(10) + {11}x^(11) + {12}x^(12) + {13}x^(13)'.format(*self.coefficent_list)) # for 14 shares



