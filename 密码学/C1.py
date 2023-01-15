import hashlib

S = "c22a563acc2a587afbfaaaa6d67bc6e628872b00bd7e998873881f7c6fdc62fc"
print(len(S))
for i in range(0, 10000):
    for j in range(0, 10000):
        s = "86170" + str(i) + str(j)
        s1 = hashlib.sha256()
        s1.update(bytes(s, encoding='utf-8'))
        b = s1.hexdigest()
        if b == S:
            print(s)
            break
