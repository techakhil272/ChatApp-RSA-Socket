import socket
# from Crypto.PublicKey import RSA
import socketrsa as sr
import rsa
HOST = '192.168.0.105'
PORT = 8989
akhilKey = sr.akhilKey()
# print(type(akhilKey))
# print(akhilKey)
jaiPub, jaiPriv = sr.loadKeys()

#print(jaiPub,'\n',jaiPriv)
# print(jaiPub)
# print('====')
# print(jaiPriv)
# afinet ip version 4
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        text=input("Enter a message : ")
        ciphertext= rsa.encrypt(text.encode('utf-8'),jaiPub)
        #print(bytes(ciphertext))
        mesg=rsa.decrypt(ciphertext,jaiPriv).decode('utf-8')
        print(mesg)
        s.sendall(ciphertext)
        data = s.recv(1024)
        akhilcipher = data
        #print(akhilcipher)
        akhilMesg = rsa.decrypt(akhilcipher,jaiPriv).decode('utf-8')
        print('Received : ',akhilMesg)
        
# repr files to string