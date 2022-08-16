import jwt
#private_key = b"-----BEGIN PRIVATE KEY-----\nMC4CAQAwBQYDK2VwBCIEIE9qP+IEtdLz8K4bG7uyN+paQwaVeqfcdr85/bP8yjY/\n-----END PRIVATE KEY-----\n"
public_key = b"-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAV+f59CntZKJJeOHI1JGzbM7ls4De6zY05g4BTNhnVpE=\n-----END PUBLIC KEY-----\n"  # Mine



payload = {
    'sub': 'my_user',
    'expi': 'hey',
}


#encoded = jwt.encode(payload, private_key, algorithm="EdDSA")
#print(encoded)

encoded = b'eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJFZERTQSIsICJjcnYiOiAiRWQyNTUxOSJ9.eyJzdWIiOiAibXlfdXNlciIsICJleHBpIjogImhleSJ9.mpPB0Ze0HKNhh6YjuODMzVpHgqIhIqDBZrn7AU7t93YZ7j_7lTX_rRf81tf1aT96htWViw9p15oirCrf6x7kBQ'
decoded = jwt.decode(encoded, public_key, algorithms=["EdDSA"])


print(decoded)



############# This script proves that my implementation of TSS EdDSA works with a python JWT lib