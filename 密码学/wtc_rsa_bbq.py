import libnum
import rsa
from Crypto.Util.number import bytes_to_long, long_to_bytes

with open(r'C:\Users\Noky-han\Desktop\cry200\key.pem') as f1:
    pubkey1 = rsa.PublicKey.load_pkcs1_openssl_pem(f1.read())
c1 = bytes_to_long(open(r"C:\Users\Noky-han\Desktop\cry200\cipher.bin", 'rb').read())
c2=open(r"C:\Users\Noky-han\Desktop\cry200\cipher.bin", 'rb').read()
print(pubkey1)
e1=pubkey1.e
n1=pubkey1.n
print("c1:", c1)
print("e1:",pubkey1.e)
print("n1:",pubkey1.n)
qss=int(open(r'C:\Users\Noky-han\Desktop\cry200\q.txt').read())
pss=int(open(r'C:\Users\Noky-han\Desktop\cry200\p.txt').read())
phi=(qss-1)*(pss-1)
d = libnum.invmod(e1, phi)
#privatekey = rsa.PrivateKey(n1, e1, d, pss, qss)
res = long_to_bytes(pow(c1, d, n1)).decode()
print(res)