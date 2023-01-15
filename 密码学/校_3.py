import libnum

s = "szzyfimhyzd"
numlsit = []
flaglist=[]
for i in s:
    numlsit.append(ord(i) - 97)
print(numlsit)
for num in numlsit:
    for j in range(0,26):
        if (j*17-8)%26==num:
            flaglist.append(j)
print(flaglist)
p=" "
for flag in flaglist:
    p=p+chr(flag+97)
print(p)
