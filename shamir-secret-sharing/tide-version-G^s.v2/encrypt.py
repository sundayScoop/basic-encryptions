from polynomial import polynomial
from orc import Orc

class Encrypt:
    def run(g):
        print("Let's create a polynomial")
        share_amount = int(input("Enter how many shares will be required to build reconstruct the secret: "))
        exponent_count = 0
        coefficient_list = []

        print("NOTE!!! Coefficient for x^0 will be your secret!")

        secret_number = int(input(f"Enter secret number to encrypt: "))

        p = polynomial(secret_number, share_amount)
        p.generate_random_coefficients()

        share_gen_amount = int(input("Time to generate some shares. Input how many shares you would like to produce: "))

        shares = p.get_shares(share_gen_amount)

        print("ORIGINAL POLYNOMIAL POINTS")
        print(shares)
        print("ORIGINAL POLY POINTS END")

        return shares
    
    def create_orcs(share_list, g, p):
        orc_list = []

        for share in share_list:
            orc = Orc(share, g, p)
            orc_list.append(orc)
        return orc_list


