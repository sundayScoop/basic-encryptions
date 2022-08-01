from random import randint

from itsdangerous import base64_encode
from polynomial import polynomial
from point import Point
import hashlib
import binascii
import base64
from ecdsa import der
import schnorr_lib
import sys




Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424

m = 115792089237316195423570985008687907853269984665640564039457584007908834671663
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337


p = polynomial(0, 7, m)

G = Point(Gx, Gy)

priv_key = 102987336249554097029535212322581322789799900648198034993379397001115665086549
privkey_hex = "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855"

pub_key = G * priv_key # This works

print("--------")
print(pub_key.x)
print(pub_key.y)
print("--------")

k = randint(1, m)
#k = 123456789

message = b"12345678901234567890123456789012"
#bin = binascii.unhexlify(message)
hash = hashlib.sha256(message).digest()
hash2 = hashlib.sha256(hash).hexdigest()

message_hash_decimal = int(hash2, 16) # This works
print("HASH: " + str(message_hash_decimal))

## Signature
R = G * k


r: int = R.x % n # Works
s: int = (pow(k, -1, n)*(message_hash_decimal + (priv_key*r))) % n # Works

print("R: " + str(r))
print("S: " + str(s))

# checks to make sure it is lower s value
if s > n/2: s = n - s # Works


# Convert to base64

final = der.encode_sequence(der.encode_integer(r), der.encode_integer(s))
finalllll = final.hex()
print("DER: " + finalllll)
print("SIGNATURE???: " + str(base64_encode(final)))




## Verify

point1 = G * (pow(s, -1, n)*message_hash_decimal)
point2 = pub_key * ((pow(s, -1, n)*r))

point3 = point1 + point2

print(point3.x)
print(R.x)





n = 28
nn = n.to_bytes(1, 'little')
#nn = n.to_bytes(1, 'big')

rb = r.to_bytes(32, 'little')
sb = s.to_bytes(32, 'little')

#rb = r.to_bytes(32, 'big')
#sb = s.to_bytes(32, 'big')

b_array = bytearray(nn)
b_array = b_array + (bytearray(rb))
b_array = b_array + (bytearray(sb))



print(sb)

sig_hex = base64.b64encode(b_array)

print(sig_hex)




