from polynomial import polynomial
from orc import Orc

class Encrypt:
    def run():
        print("Let's create a polynomial")
        share_amount = int(input("Enter how many shares will be required to build reconstruct the secret: "))
        exponent_count = 0
        coefficient_list = []

        print("NOTE!!! Coefficient for x^0 will be your secret!")

        secret_number = float(input(f"Enter secret number to encrypt: "))

        p = polynomial(secret_number, share_amount)

        share_gen_amount = int(input("Time to generate some shares. Input how many shares you would like to produce: "))

        shares = p.get_shares(share_gen_amount)

        other_secret_number = int(input("Enter number to confuse decryptor: "))

        print("Here are the shares in terms of (x,y): ")
        print(shares)

        return [shares, share_amount, share_gen_amount, other_secret_number]
    
    def create_orcs(share_list, t, n, other_secret_number):
        orc_list = []
        for share in share_list:
            orc = Orc(share, t, n, other_secret_number)
            orc_list.append(orc)
        return orc_list


