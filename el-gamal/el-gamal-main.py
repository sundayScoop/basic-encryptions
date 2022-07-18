g = 2
print("G is ", g)
bob_random_number = int(input("Enter Bob's random number: "))
bob_pub_key = pow(g, bob_random_number)
print(bob_pub_key)

## Send bob's pub key to alice

message = int(input("Enter Alice's secret message (digits): "))
alice_random_number = int(input("Enter Alice's random number: "))
alice_pub_key = pow(g, alice_random_number)
print(alice_pub_key)

## Encryption
encrypted_message = message * pow(bob_pub_key, alice_random_number)
print(encrypted_message)

## Send encrypted message and alice pub key to bob

decrypted_message = encrypted_message / pow(alice_pub_key, bob_random_number)

print(decrypted_message)