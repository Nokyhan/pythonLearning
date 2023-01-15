from shlex import join

cipher = "frxnimpqil"
cipher1="opkxu"
cipher2="bju"
obviouscode = "betweenand"
obviouscode1="theth"
obviouscode2="the"
cipher_list=list(cipher)
cipher_list1=list(cipher1)
cipher_list2=list(cipher2)
obviouscode_list=list(obviouscode)
obviouscode_list1=list(obviouscode1)
obviouscode_list2=list(obviouscode2)
#print(cipher_list)
print(ord('f')-ord('b'))
a=[]
for i in range(len(cipher)):
    m=(ord(cipher_list[i])-ord(obviouscode_list[i]))%26
    a.append(chr(m+ord('A')))
print(join(a))
b=[]
for i in range(len(cipher1)):
    m=(ord(cipher_list1[i])-ord(obviouscode_list1[i]))%26
    b.append(chr(m+ord('A')))
print(join(b))
c=[]
for i in range(len(cipher2)):
    m=(ord(cipher_list2[i])-ord(obviouscode_list2[i]))%26
    c.append(chr(m+ord('A')))
print(join(c))