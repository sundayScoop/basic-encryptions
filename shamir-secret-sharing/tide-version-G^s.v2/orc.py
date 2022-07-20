class Orc:
    def __init__(self, point, g) -> None:
        self.orc_x = point[0]
        self.orc_y = point[1]
        self.orc_xs_list = []
        self.g = g

    def get_orc_share(self): # Math involved
        j = 0
        k = len(self.orc_xs_list)
        multiplication = 0

        multiplication = self.orc_y
        while j < k:
            if self.orc_xs_list[j] != self.orc_x: multiplication = multiplication * (self.orc_xs_list[j]/(self.orc_xs_list[j] - self.orc_x))
            j+=1
        
        result = pow(self.g, multiplication) # Raise G to the calculation
        
        return result # The secret
    
    def update_orc_list(self, orc_xs_list):
        self.orc_xs_list = orc_xs_list
    
    def get_orc_x(self):
        return self.orc_x