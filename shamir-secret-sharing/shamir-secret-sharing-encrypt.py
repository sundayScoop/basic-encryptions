from polynomial import polynomial


print("Let's create a polynomial")
share_amount = int(input("Enter how many shares will be required to build reconstruct the secret: "))
exponent_count = 0
coefficient_list = []

print("NOTE!!! Coefficient for x^0 will be your secret!")

while exponent_count < share_amount:
    coefficient_list.append(float(input(f"Enter coefficient at x^{exponent_count}: ")))
    exponent_count+=1

p = polynomial(coefficient_list)

share_gen_amount = int(input("Time to generate some shares. Input how many shares you would like to produce: "))

shares = p.get_shares(share_gen_amount)

print("Here are the shares in terms of (x,y): ")
print(shares)



