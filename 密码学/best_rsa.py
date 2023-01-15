import libnum
import rsa
from Crypto.Util.number import bytes_to_long, long_to_bytes
from gmpy2 import gmpy2
from numpy import invert


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


with open(r'C:\Users\Noky-han\Desktop\publickey1.pem') as f1:
    pubkey1 = rsa.PublicKey.load_pkcs1_openssl_pem(f1.read())
with open(r'C:\Users\Noky-han\Desktop\publickey2.pem') as f2:
    pubkey2 = rsa.PublicKey.load_pkcs1_openssl_pem(f2.read())
c1 = bytes_to_long(open(r'C:\Users\Noky-han\Desktop\cipher1.txt', 'rb').read())
c2 = bytes_to_long(open(r'C:\Users\Noky-han\Desktop\cipher2.txt', 'rb').read())
print("c1:", c1)
print("e1: ", pubkey1.e)
print("n1: ", pubkey1.n)
# print("c1: "+str(c1))
print("c2:", c2)
print("e2: ", pubkey2.e)
print("n2: ", pubkey2.n)
e1 = pubkey1.e
e2 = pubkey2.e
n = pubkey1.n
c1 = bytes_to_long(open(r'C:\Users\Noky-han\Desktop\cipher1.txt', 'rb').read())
c2 = bytes_to_long(open(r'C:\Users\Noky-han\Desktop\cipher2.txt', 'rb').read())

# print("c2: "+str(c2))
# 可以得出是共模攻击

_, r, s = gmpy2.gcdext(e1, e2)

#
m = pow(c1, r, n) * pow(c2, s, n) % n
print(m)
print(long_to_bytes(m).decode())
