from secret_reconstructor import secret_reconstructor

print("\n--------------------------------------------")
print("Now let's recontruct the secret from some shares")

share_amount = int(input("Enter how many shares you have: "))
share_count = 0
share_list = []

while share_count < share_amount:
    print("------------------------------------")
    x_point = float(input(f"Enter x_coordinate for point {share_count}: "))
    y_point = float(input(f"Enter y_coordinate for point {share_count}: "))
    
    point = (x_point, y_point)

    share_list.append(point)
    share_count+=1

print("Shares collected!")

c = secret_reconstructor(share_list)

secret = c.get_secret()

print(secret)
