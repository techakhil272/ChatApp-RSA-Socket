from cgitb import text
import socket
import socketrsa as sr
HOST = '192.168.0.112'
PORT =  7896

jaiPub , jaiPriv = sr.loadKeys()
akhilPub = sr.akhilKey()

def conn_chat(a):
    conn, addr = a.accept()
    print('Connected by', addr)
    while True:
            akhilCipher = conn.recv(1024)
            akhilMesg = sr.decrypt(akhilCipher, jaiPriv)
            print("Received",akhilMesg)

            text = input("Send a message: ")
            ciphertext = sr.encrypt(text,akhilPub)
            conn.sendall(ciphertext)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn_chat(s)


input("enter")
