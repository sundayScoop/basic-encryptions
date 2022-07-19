from encrypt import Encrypt
from decrypt import Decrypt

e = Encrypt

encrypt_info = e.run()

## Get orcs
orc_list = e.create_orcs(encrypt_info[0], encrypt_info[1], encrypt_info[2], encrypt_info[3])

print("Decrypting.....................")
d = Decrypt(orc_list).run()
