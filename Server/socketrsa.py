import rsa as rs

def generateKeys():
    (publicKey, privateKey) = rs.newkeys(1024)
    with open('keys/jaiPub.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/jaiPriv.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
    with open('keys/jaiPub.pem', 'rb') as p:
        publicKey = rs.PublicKey.load_pkcs1(p.read())
    with open('keys/jaiPriv.pem', 'rb') as p:
        privateKey = rs.PrivateKey.load_pkcs1(p.read())
    return publicKey, privateKey

def encrypt(message, key):
    return rs.encrypt(message.encode('utf-8'), key)

def decrypt(ciphertext, key):
    return rs.decrypt(ciphertext, key).decode('utf-8')
    

def akhilKey():
    with open('keys/akhilPub.pem', 'rb') as p:
        MartinPub = rs.PublicKey.load_pkcs1(p.read())
    return MartinPub

#generateKeys()
# publicKey, privateKey = loadKeys()

# message = input('Write your message here:')
# ciphertext = encrypt(message, publicKey)

# signature = sign(message, privateKey)

# text = decrypt(ciphertext, privateKey)

# print(f'Cipher text: {ciphertext}')
# print(f'Signature: {signature}')

# if verify(text, signature, publicKey):
#     print('Successfully verified signature')
# else:
#     print('The message signature could not be verified')