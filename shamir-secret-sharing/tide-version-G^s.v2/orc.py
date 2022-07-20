class Orc:
    def __init__(self, point, g, p) -> None:
        self.orc_x = point[0]
        self.orc_y = point[1]
        self.orc_xs_list = []
        self.g = g
        self.p = p

    def get_orc_share(self): # Math involved
        j = 0
        k = len(self.orc_xs_list)
        multiplication: int = 0

        multiplication = self.orc_y
        while j < k:
            if self.orc_xs_list[j] != self.orc_x: 
                x_calc_result:float = (self.orc_xs_list[j]/(self.orc_xs_list[j] - self.orc_x))
                a: int = 0
                b: int = 0
                number: int = 0
                a, b = x_calc_result.as_integer_ratio()
                number, residual = divmod(multiplication * a, b)
                multiplication = number
            j+=1
        
        print("_____________")
        print(self.g)
        print(multiplication)
        print("_____________")
        result = pow(self.g, int(multiplication), self.p) # Raise G to the calculation mod m
        
        return result # The secret
    
    def update_orc_list(self, orc_xs_list):
        self.orc_xs_list = orc_xs_list
    
    def get_orc_x(self):
        return self.orc_x