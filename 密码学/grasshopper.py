from Crypto.Util.number import *
from random import randrange

f = open(r"D:\EdgeDownload\grasshopper_e10b36fdd01d4b51d6867b1588afade7\output.txt")
s = f.read()
s = s.split()
print(s[1])
p = getPrime(16)
flag = []
for ppp in range(100000):
    k = [randrange(1, p) for i in range(5)]
    print(flag)
    for i in range(len(s)):
        for grasshopper in range(10):
            for j in range(5):
                k[j] = grasshopper = grasshopper * k[j] % p
            ssp = 'Grasshopper#' + str(i).zfill(2) + ':' + hex(grasshopper)[2:].zfill(4)
            if ssp == s[i]:
                flag.append(grasshopper)
    print(flag)
