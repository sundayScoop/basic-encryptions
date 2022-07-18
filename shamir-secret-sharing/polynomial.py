import random

class polynomial:
    def __init__(self, coefficient_list) -> None:
        self.coefficent_list = coefficient_list
        self.y_intercept = coefficient_list[0]
    
    def get_y_position(self, x_position):
        y_position = self.coefficent_list[0] # y_intercept
        exponent_count = 1 # e.g. x^1 . y_position above would be x^0 (1), so just the y_interecept (first item) 

        for coefficient in self.coefficent_list[1:]: # [1:] because [0] has already been included in calc. above
            y_position = y_position + coefficient*pow(x_position, exponent_count)  # Change + to +/- option depending on coefficient
            exponent_count+=1
            

        return y_position
    
    def get_shares(self, share_amount: int) -> list:
        share_list = []

        for i in range(share_amount):
            random_x_point = random.randint(1, 10) # Generate random int for point x
            y_point = self.get_y_position(random_x_point)

            point = (random_x_point, y_point)

            share_list.append(point)
        
        return share_list