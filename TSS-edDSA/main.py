
from sharer import Sharer

share_num = 3
x_list = list(range(1, share_num+1)) # [1,2]


## Create CMK
sharer = Sharer(x_list)
sharer.createOrks()
print(sharer.createCMK()) # Good! Able to be interpolated. Times it by G now

msg_to_sign = input("Enter the message you wish to sign: ")



