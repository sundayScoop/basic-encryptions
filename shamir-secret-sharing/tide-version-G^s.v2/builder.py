from orc import Orc

class Builder:
    def __init__(self, orc_list, share_amount) -> None:
        self.orc_list = orc_list
        self.share_amount = share_amount
        self.point_list = []
    
    def request_orc_shares(self):
        print("ORC LIST BELOW")
        i = 0
        for orc in self.orc_list:
            share = orc.get_share()
            print(share)
            self.point_list.append(share)
            i+=1
            if i >= self.share_amount: break # Only query specific number of orcs as per user request
        print("ORC LIST END") 
    
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
                