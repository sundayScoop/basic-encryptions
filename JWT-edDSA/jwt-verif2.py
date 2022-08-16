import python_jwt as jwt, jwcrypto.jwk as jwk, datetime
import json
from base64 import urlsafe_b64encode


def b64encode_nopadding(to_encode):
    return urlsafe_b64encode(to_encode).rstrip(b'=')


key = {
    "kty":"OKP",
    "use":"sig",
    "crv":"Ed25519",
    "kid":"38be7f68-3765-43f9-a257-414be2cf2f7c",
    "x":"V-f59CntZKJJeOHI1JGzbM7ls4De6zY05g4BTNhnVpE"
}


payload = {
    'sub': 'my_user',
    'exp': 3475878357,
}


key = jwk.JWK.from_json(json.dumps(key))
print(key.export_to_pem())

############################### This script is used to convert my JWK key (easy to create from an encoded point) to a PEM key used in the other JWT scripts