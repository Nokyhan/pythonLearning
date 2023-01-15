from Crypto.PublicKey import RSA
from base64 import b64decode
from gmpy2 import invert
import rsa

with open(r'C:\Users\Noky-han\Desktop\key.pub', 'rb') as file:#文件地址可以换
    f = file.read()
pub = RSA.importKey(f)
print(pub)
n = pub.n
e = pub.e

p = 863653476616376575308866344984576466644942572246900013156919
q = 965445304326998194798282228842484732438457170595999523426901
d = int(invert(e, (p - 1) * (q - 1)))

key = rsa.PrivateKey(n, e, d, p, q)

with open(r'C:\Users\Noky-han\Desktop/flag.b64', 'r') as file:
    f = file.read()
c = b64decode(f)
flag = rsa.decrypt(c, key).decode()

print(flag)
