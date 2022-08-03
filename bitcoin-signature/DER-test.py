from random import randint


from polynomial import polynomial
from point import Point
import hashlib
import binascii
import base64
import sys
from f_msg import Msg_Requester




Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424

m = 115792089237316195423570985008687907853269984665640564039457584007908834671663
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337


p = polynomial(0, 7, m)

G = Point(Gx, Gy)

priv_key = 102987336249554097029535212322581322789799900648198034993379397001115665086549 #this works
privkey_hex = "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855" #this works



pub_key = G * priv_key # This works definately!

print("--------")
print(pub_key.x)
print(pub_key.y)
print("--------")

k = randint(1, m)
#k = 123456789


#Sktech
message_hash_decimal = Msg_Requester.getMsg()

## Signature
R = G * k


r: int = R.x % n # Works
s: int = (pow(k, -1, n)*(message_hash_decimal + (priv_key*r))) % n # Works



# checks to make sure it is lower s value
if s > n/2: s = n - s # Works


# Sktech
#r = 10812059355684102320433147997847874770455099645674156258324787660491311276333
#s = 1139044670623009341183358904162604827072884806515105648340258540807353884833

##


print("R: " + str(r))
print("S: " + str(s))


## Verify

point1 = (pow(s, -1, n)*message_hash_decimal) % n
point2 = ((pow(s, -1, n)*r)) % n

point3 = (G * point1) + (pub_key * point2)

print((r == point3.x % n))


##
#r = 100000000000
#s = 100
##

i = 0
n = 27
for i in range(3):
   
    
    nn = n.to_bytes(1, 'big')
    #nn = n.to_bytes(1, 'big')

    rb = r.to_bytes(32, 'big')
    sb = s.to_bytes(32, 'big')

    #rb = r.to_bytes(32, 'big')
    #sb = s.to_bytes(32, 'big')

    b_array = bytearray(nn)
    b_array = b_array + (bytearray(rb))
    b_array = b_array + (bytearray(sb))

    sig_hex = base64.b64encode(b_array)

    print(str(sig_hex))
    n +=1




