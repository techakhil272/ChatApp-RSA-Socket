import socket
# from Crypto.PublicKey import RSA
import socketrsa as sr
HOST = '192.168.0.112'
PORT = 8990
jaiPub = sr.jaiKey()
# print(type(akhilKey))
# print(akhilKey)
akhilPub, akhilPriv = sr.loadKeys()

#print(jaiPub,'\n',jaiPriv)
# print(jaiPub)
# print('====')
# print(jaiPriv)
# afinet ip version 4
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        text=input("Enter a message : ")
        ciphertext= sr.encrypt(text,jaiPub)
        #print(bytes(ciphertext))
        s.sendall(ciphertext)
        data = s.recv(1024)
        #print(akhilcipher)
        akhilMesg = sr.decrypt(data,akhilPriv)
        print('Received : ',akhilMesg)
        
# repr files to string