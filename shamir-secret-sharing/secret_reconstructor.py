class secret_reconstructor:
    def __init__(self, point_list) -> None:
        self.point_list = point_list
    
    def get_secret(self): # Math involved
        j = 0
        k = len(self.point_list)
        sum = 0
        multiplication = 0

        while j < k:
            m = 0
            multiplication = self.point_list[j][1] # Get y_point of point_list[j]
            while m < k:
                if m != j: multiplication = multiplication * (self.point_list[m][0]/(self.point_list[m][0] - self.point_list[j][0]))
                m+=1
            sum = sum + multiplication
            j+=1
        
        return sum # The secret
                