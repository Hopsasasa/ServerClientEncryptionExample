
g = 42
p = 29837
pk = 22690 # public key
c1 = 23447 # message 1
c2 = 8372 # message 2

# A function to bruteforce the private key using the public information
def bruteforcePrivateKey(g, p, publicKey):
    for x in range(p):
        calc = pow(g, x) % p
        if (calc == publicKey):
            return x
    return -1 # Could not find the private key

# A function to decrypt the encrypted message using the private key
def decryptMessage(p, privateKey, c1, c2):
    sharedSecret = pow(c1, privateKey) % p
    sharedInverse = pow(sharedSecret, p - 2) % p
    message = c2 * sharedInverse % p
    return message

# A function that modifies the encrypted message to decrypt into a specific number
def modifyMessage(encryptedMessage, decryptedMessage, modifiedMessage, p):
    ratio = (modifiedMessage * (pow(decryptedMessage, p-2) % p)) % p
    return (encryptedMessage * ratio) % p

privateKey = bruteforcePrivateKey(g, p, pk) # should give 24774
print("Private Key: " + str(privateKey))
message = decryptMessage(p, privateKey, c1, c2)
print("Student Number: " + str(message))
studenNumber = 22304 # my student number
modifiedMessage = modifyMessage(c2, message, studenNumber, p)
print("Modified encrypted message: " + str(modifiedMessage))
decryptedModifiedMessage = decryptMessage(p, privateKey, c1, modifiedMessage)
print("Modified student number: " + str(decryptedModifiedMessage))