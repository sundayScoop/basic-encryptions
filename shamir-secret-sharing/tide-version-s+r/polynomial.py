import random

class polynomial:
    def __init__(self, secret_number, share_amount) -> None:
        self.y_intercept = secret_number
        self.coefficent_list = [self.y_intercept]
        self.share_amount = share_amount - 1 # -1 because y_intercept coffecient already included

    
    def set_up_object_for_random_polynomial(self): # Deletes y intercept as it'll be random and +1 on share amount to accomodate for how many shares to produce, not including previous y-intercept
        self.coefficent_list = []
        self.share_amount = self.share_amount+1
    
    def generate_random_coefficients(self):
        for i in range(self.share_amount):
            coefficient = random.randint(-10, 10)
            self.coefficent_list.append(coefficient)
        print("COEFFICIENT LIST")
        print(self.coefficent_list)
        print("COEFFICIENT LIST END")
    
    def get_y_position(self, x_position):
        y_position = self.coefficent_list[0] # y_intercept
        exponent_count = 1 # e.g. x^1 . y_position above would be x^0 (1), so just the y_interecept (first item) 

        for coefficient in self.coefficent_list[1:]: # [1:] because [0] has already been included in calc. above
            y_position = y_position + coefficient*pow(x_position, exponent_count)  
            exponent_count+=1
            

        return y_position
    
    def get_shares(self, share_amount: int) -> list:
        share_list = []
        x_point = 2

        for i in range(share_amount):
            y_point = self.get_y_position(x_point)

            point = (x_point, y_point)

            share_list.append(point)

            x_point+=1
        
        return share_list