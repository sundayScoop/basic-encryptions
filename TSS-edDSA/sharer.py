from ork import Ork
from point import Point

class Sharer:
    def __init__(self, x_list, G: Point, p:int, order: int) -> None:
        self.x_list = x_list
        self.G = G
        self.ork_list = []
        self.p = p
        self.order = order
    
    def createOrks(self):
        i = 0
        for x in self.x_list:
            self.ork_list.append(Ork(self.x_list, x, self.G, self.p, self.order))
            i+=1
        return self.ork_list
    
    def createCMK(self) -> Point:
        y_list_for_all_xs_all_polynomials = {} # Get values to be exchanged from orks
        for ork in self.ork_list:
            ork.generate_random_polynomial()
            y_list_for_all_xs_all_polynomials[ork.getMyX()] = ork.get_this_orks_ys_at_other_x_points()
        
        for ork in self.ork_list: # Exchange values between orks
            y_list = []
            for ork_o in y_list_for_all_xs_all_polynomials:
                if ork_o != ork.getMyX(): # Ork 1's Y list will not contain y value at x=1 as it is secret
                    y_list.append(y_list_for_all_xs_all_polynomials[ork_o][ork.getMyX()]) # Doesn't care about X values, as they're all the same for this ork's y_list. Just need the Y's
            ork.set_other_orks_y_list(y_list)
        
        # get public key from partial private keys * G
        public_key: Point = self.ork_list[0].get_partial_pub_key()
        for ork in self.ork_list[1:]:
            public_key = public_key + ork.get_partial_pub_key()
        return public_key
    
    def get_ork_random_numbers(self):
        random_shares = []
        for ork in self.ork_list:
            random_shares.append(ork.get_random_polynomial_point())

        return random_shares
