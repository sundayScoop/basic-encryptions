import base64
import hashlib
import binascii
import base64
import sys

class Msg_Requester:
    def getMsg():
        input("Make sure to add num_list from JS script into f_msg.py")
        #
        msg_array = [24,66,105,116,99,111,105,110,32,83,105,103,110,101,100,32,77,101,115,115,97,103,101,58,10,5,74,117,108,105,111]
        msg_bytes = bytes(msg_array)
        hash = hashlib.sha256(msg_bytes).digest()
        hash2 = hashlib.sha256(hash).hexdigest()

        #print("DEC: " + str(int.from_bytes(hash2, 'big')))

        message_hash_decimal = int(hash2, 16) # This definately worksssss
        print("HASH: " + str(message_hash_decimal))
        return message_hash_decimal


