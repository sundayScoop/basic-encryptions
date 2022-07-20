from orc import Orc

class Builder:
    def __init__(self, orc_list, share_amount) -> None:
        self.orc_list = orc_list
        self.share_amount = share_amount
        self.share_list = []
    
    def request_orc_shares(self):
        print("ORC LIST BELOW")
        i = 0
        for orc in self.orc_list:
            share = orc.get_orc_share()
            print(share)
            self.share_list.append(share)
            i+=1
            if i >= self.share_amount: break # Only query specific number of orcs as per user request
        print("ORC LIST END") 
    
    def generate_orc_secrets(self): # Math involved
        result = 1

        for share in self.share_list: # Multiply all orc shares together
            result = result * share
        
        return result
                