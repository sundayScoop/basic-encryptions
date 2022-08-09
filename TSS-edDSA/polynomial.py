import random

class Polynomial:
    def __init__(self, threshold) -> None:
        self.coefficent_list = []
        self.threshold = threshold
    
    def get_y_position(self, x_position):
        y_position = self.coefficent_list[0] # y_intercept
        exponent_count = 1 # e.g. x^1 . y_position above would be x^0 (1), so just the y_interecept (first item) 

        for coefficient in self.coefficent_list[1:]: # [1:] because [0] has already been included in calc. above
            y_position = y_position + coefficient*pow(x_position, exponent_count)  # Change + to +/- option depending on coefficient
            exponent_count+=1
            

        return y_position
    
    def generate_random_coefficients(self):
        for i in range(self.threshold):
            self.coefficent_list.append(random.randint(1, 4))
        print("Rand c_list: " + str(self.coefficent_list))



