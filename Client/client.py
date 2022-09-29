import socket
import socketrsa as sr

HOST = '172.20.82.17'
PORT = 7896

akhilPub,akhilPriv = sr.loadKeys()
jaiPub = sr.jaiKey()

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        text=input("Enter a message : ")
        ciphertext= sr.encrypt(text,jaiPub)
        s.sendall(ciphertext)
        
        data = s.recv(1024)
        akhilMesg = sr.decrypt(data,akhilPriv)
        print('Received : ',akhilMesg)
