from ork import Ork

class Sharer:
    def __init__(self, x_list, g) -> None:
        self.x_list = x_list
        self.g = g
        self.ork_list = []
    
    def createOrks(self):
        i = 0
        for x in self.x_list:
            self.ork_list.append(Ork(self.x_list, x, self.g))
            i+=1
        return self.ork_list
    
    def createCMK(self):
        y_list_for_all_xs_all_polynomials = {}
        for ork in self.ork_list:
            ork.generate_random_polynomial()
            y_list_for_all_xs_all_polynomials[ork.getMyX()] = ork.get_this_orks_ys_at_other_x_points()
        
        for ork in self.ork_list:
            y_list = []
            for ork_o in y_list_for_all_xs_all_polynomials:
                if ork_o != ork.getMyX(): # Ork 1's Y list will not contain y value at x=1 as it is secret
                    y_list.append(y_list_for_all_xs_all_polynomials[ork_o][ork.getMyX()]) # Doesn't care about X values, as they're all the same for this ork's y_list. Just need the Y's
            ork.set_other_orks_y_list(y_list)
        
        random_shares = []
        for ork in self.ork_list:
            random_shares.append(ork.get_random_polynomial_point())

        return random_shares
