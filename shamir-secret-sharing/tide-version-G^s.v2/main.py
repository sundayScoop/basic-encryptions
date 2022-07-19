from encrypt import Encrypt
from decrypt import Decrypt

e = Encrypt

g = 2

share_list = e.run(g)

## Get orcs
orc_list = e.create_orcs(share_list, g)

print("Decrypting.....................")
d = Decrypt(orc_list).run()
