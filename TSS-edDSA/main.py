
from hashlib import sha3_512
import hashlib
from sharer import Sharer
from ork import Ork

share_num = 2
x_list = list(range(1, share_num+1)) 

g = 2


## Create CMK
sharer = Sharer(x_list, g)
orc_list = sharer.createOrks()


print(sharer.createCMK()) # Good! Able to be interpolated. Times it by G now

msg_to_sign = input("Enter the message you wish to sign: ")


# Begin signing process

# get randoms from orks
Gr = 1
for orc in orc_list:
    Gr = Gr * orc.generate_random_number()

print(Gr)

# generating e
#hash_data = bytes(Gr)
#hash_data += bytes(msg_to_sign.encode('utf-8'))

#e = hashlib.sha256(hash_data).hexdigest()
e = '1'



# generating S. Remeber the orks do this as the private key is split up amonst them
s = 0
for orc in orc_list:
    s = s + orc.sign_message(msg_to_sign, Gr)
    print("partials : " + str(s))

print("S: " + str(s))

## Verification

Gk = 1 # Pub key
for orc in orc_list:
    Gk = Gk * orc.get_partial_pub_key()



Ry: int = pow(g, s) * pow(Gk, int(e, 16))

print(Ry == Gr) # This is a hack. But it proves the signature is valid



