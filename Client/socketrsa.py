import rsa as rs

def generateKeys():
    (publicKey, privateKey) = rs.newkeys(1024)
    with open('keys/akhilPub.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/akhilPriv.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
    with open('keys/akhilPub.pem', 'rb') as p:
        publicKey = rs.PublicKey.load_pkcs1(p.read())
    with open('keys/akhilPriv.pem', 'rb') as p:
        privateKey = rs.PrivateKey.load_pkcs1(p.read())
    return publicKey, privateKey

def encrypt(message, key):
    return rs.encrypt(message.encode('utf-8'), key)

def decrypt(ciphertext, key):
    return rs.decrypt(ciphertext, key).decode('utf-8')
    
def jaiKey():
    with open('keys/jaiPub.pem', 'rb') as p:
        jaiPub = rs.PublicKey.load_pkcs1(p.read())
    return jaiPub

#generateKeys()
