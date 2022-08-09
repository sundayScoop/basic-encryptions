
from hashlib import sha3_512
import hashlib
from sharer import Sharer
from ork import Ork
from point import Point

share_num = 14
x_list = list(range(1, share_num+1)) 

# Ed25519 Parametres
Gx = 15112221349535400772501151409588531511454012693041857206046113283949847762202
Gy = 46316835694926478169428394003475163141307993866256225615783033603165251855960

G = Point(Gx, Gy)

p = 57896044618658097711785492504343953926634992332820282019728792003956564819949 # 2**255 -19
order = 7237005577332262213973186563042994240857116359379907606001950938285454250989






## Create CMK
sharer = Sharer(x_list, G, p, order)
orc_list = sharer.createOrks()

public_key: Point = sharer.createCMK() # Good! Able to be interpolated. Times it by G now
print("Public X " + str(public_key.x))

#print(sharer.get_ork_random_numbers())

'''
lan = 0
for orc in orc_list:
    lan = lan + orc.get_partial_key()   
lan = lan % p

print(lan)    ## Whoop Whoop! THIS IS THE CMK. DO NOT EXPOSE AHGHHHHH
'''

msg_to_sign = input("Enter the message you wish to sign: ")


# Begin signing process

# get random points from orks
r: Point = orc_list[0].generate_random_point() # R public

for orc in orc_list[1:]:
    r = r + orc.generate_random_point()

print("R.x" + str(r.x))

# generating e
# hash will be H(r.x, r.y, message)
rx_bytes = r.x.to_bytes(32, 'little')             # Little endian!!!! edDSA encoding standard
ry_bytes = r.y.to_bytes(32, 'little')
msg_bytes = bytes(msg_to_sign.encode())

hash_data = rx_bytes
hash_data += ry_bytes
hash_data += msg_bytes


#hash_data = bytes(Gr)
#hash_data += bytes(msg_to_sign.encode('utf-8'))

e = int(hashlib.sha256(hash_data).hexdigest(), 16) % order # int value of 32 byte hash
print("Client e: " + str(e))


# generating S. Remeber the orks do this as the private key is split up amonst them
s = 0 # S public
for orc in orc_list:
    s = s + orc.sign_message(msg_to_sign, r)
s = s % order

print("S: " + str(s))

## Verification
point1 = G * s
point2 = r + (public_key * e)

#Ry: Point = (G * s) + (public_key * e) 


print(point1.x == point2.x) # This is a hack. But it proves the signature is valid


