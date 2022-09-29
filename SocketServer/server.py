
import socket
import socketrsa as sr
HOST = '192.168.0.103'
PORT = 12321
# def jaiKey():
#     with open('jaiPub.pem', 'rb') as p:
#         publicKey = rsa.PublicKey.load_pkcs1(p.read())
#     with open('jaiPriv.pem', 'rb') as p:
#         privateKey = rsa.PrivateKey.load_pkcs1(p.read())
#     return publicKey, privateKey
# # sr.generateKeys()
akhilPub , akhilPriv = sr.loadKeys()
jaiPub = sr.jaiKey()
# type(jaiPub)
# print(jaiPub,'/n',jaiPriv)
#akhilPub, akhilPriv = sr.loadKeys()
#print(akhilPub)
# publicKey, privateKey = sr.loadKeys()
def conn_chat(a):
    print("connecting")
    conn, addr = a.accept()
    print('Connected by', addr)
    while True:
            jaiCipher = conn.recv(1024)
            #print("Received:",jaiRec)
            jaiMesg = sr.decrypt(jaiCipher, akhilPriv)
            print("Received",jaiMesg)
            text = input("Send a message: ")
            ciphertext = sr.encrypt(text, jaiPub)
            conn.sendall(ciphertext)
       
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    print("Binding")
    s.bind((HOST,PORT))
    print("Binded")
    s.listen()
    conn_chat(s)

#print(bytes(ciphertext))
            #mesg=rsa.decrypt(ciphertext,jaiPriv).decode('utf-8')
            #print(mesg)