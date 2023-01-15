import base64

import libnum
import rsa

from RSA_gcd import phi_n

with open(r'C:\Users\Noky-han\Desktop\gy.key') as f1:
    pubkey1 = rsa.PublicKey.load_pkcs1_openssl_pem(f1.read())
e1=pubkey1.e
n1=pubkey1.n
print("e1: ", pubkey1.e)
print("n1: ", pubkey1.n)
q=273821108020968288372911424519201044333
p=280385007186315115828483000867559983517
phi=(q-1)*(p-1)
#print(phi)
d = libnum.invmod(e1, phi)
print(d)
privatekey = rsa.PrivateKey(n1, e1, d, p, q)
with open(r"C:\Users\Noky-han\Desktop\fllllllag.txt", "rb") as f:
    print(rsa.decrypt(f.read(), privatekey).decode())

