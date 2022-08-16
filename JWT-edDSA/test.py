from base64 import urlsafe_b64encode
import json
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, NoEncryption, PrivateFormat, PublicFormat

def b64encode_nopadding(to_encode):
    return urlsafe_b64encode(to_encode).rstrip(b'=')

#private_key = load_pem_private_key(
    # In real cases, take the private key from an environment variable or secret store
   # b'-----BEGIN PRIVATE KEY-----\nMC4CAQAwBQYDK2VwBCIEIE9qP+IEtdLz8K4bG7uyN+paQwaVeqfcdr85/bP8yjY/\n-----END PRIVATE KEY-----\n', password=None, backend=default_backend())
#print(private_key.private_bytes(encoding=Encoding.PEM, format=PrivateFormat.PKCS8, encryption_algorithm=NoEncryption()))
#print(private_key.public_key().public_bytes(encoding=Encoding.PEM, format=PublicFormat.SubjectPublicKeyInfo))


pub_key = load_pem_public_key(
  b'-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAV+f59CntZKJJeOHI1JGzbM7ls4De6zY05g4BTNhnVpE=\n-----END PUBLIC KEY-----\n' # This one is from my program
)

header = {
    'typ': 'JWT',
    'alg': 'EdDSA',
    'crv': 'Ed25519',
}
payload = {
    'sub': 'my_user',
    'expi': 'hey',
}


to_sign = b64encode_nopadding(json.dumps(header).encode('utf-8')) + b'.' + b64encode_nopadding(json.dumps(payload).encode('utf-8'))   ## What I want to sign

print(to_sign.decode())
#signature = b64encode_nopadding(private_key.sign(to_sign)) # gotta decode sig to bytes
#sig = private_key.sign(to_sign)   

signature = bytes(bytearray.fromhex('9a93c1d197b41ca36187a623b8e0cccd5a4782a22122a0c166b9fb014eedf77619ee3ffb9535ffad17fcd6d7f5693f7a86d5958b0f69d79a22ac2adfeb1ee405')) # Paste sig here
#jwt = (to_sign + b'.' + signature)

print("To sign: " + str(to_sign))
#print("Full JWT: " + str(jwt))



verif = pub_key.verify(signature, to_sign) # Signature must be bytes object


####################### This script proves other cryptographic libs work with with implemtation of TSS EdDSA

