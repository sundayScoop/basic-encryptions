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
        p.generate_random_coefficients()

        share_gen_amount = int(input("Time to generate some shares. Input how many shares you would like to produce: "))

        shares = p.get_shares(share_gen_amount)

        print("ORIGINAL POLYNOMIAL POINTS")
        print(shares)
        print("ORIGINAL POLY POINTS END")


        random_polynomial = polynomial(1, share_amount) # y-intercept of 1 will be erased below
        random_polynomial.set_up_object_for_random_polynomial()
        random_polynomial.generate_random_coefficients()

        random_polynomial_points = random_polynomial.get_shares(share_gen_amount)

        print("RANDOM_POLYNOMIAL POINTS")
        print(random_polynomial_points)
        print("RANDOM POLY POINTS END")

        return [shares, share_amount, share_gen_amount, random_polynomial]
    
    def create_orcs(share_list, t, n, random_polynomial: polynomial):
        orc_list = []
        for share in share_list:
            orc = Orc(share, t, n, random_polynomial.get_y_position(share[0])) # Give orc y position of random polynomial at same x position as original polynomial
            orc_list.append(orc)
        return orc_list


