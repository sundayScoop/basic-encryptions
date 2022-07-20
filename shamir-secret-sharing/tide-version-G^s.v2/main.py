from encrypt import Encrypt
from decrypt import Decrypt

e = Encrypt

g = 2

p = 72348129505834630344498057854153126792908605880009





share_list = e.run(g)

## Get orcs
orc_list = e.create_orcs(share_list, g, p)

print("Decrypting.....................")
d = Decrypt(orc_list, p).run()
