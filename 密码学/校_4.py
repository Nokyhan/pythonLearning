key = "2,5,1,3,6,4,9,7,8,14,10,13,11,12"
cipher_text = "HCBTSXWCRQGLES"
f = open(r"D:\EdgeDownload\Thomas Jefferson\ge.txt")
# print(f.read())
s = ["ZWAXJGDLUBVIQHKYPNTCRMOSFE", "KPBELNACZDTRXMJQOYHGVSFUWI", "BDMAIZVRNSJUWFHTEQGYXPLOCK",
     "RPLNDVHGFCUKTEBSXQYIZMJWAO", "IHFRLABEUOTSGJVDKCPMNZQWXY", "AMKGHIWPNYCJBFZDRUSLOQXVET",
     "GWTHSPYBXIZULVKMRAFDCEONJQ", "NOZUTWDCVRJLXKISEFAPMYGHBQ", "QWATDSRFHENYVUBMCOIKZGJXPL",
     "WABMCXPLTDSRJQZGOIKFHENYVU", "XPLTDAOIKFZGHENYSRUBMCQWVJ", "TDSWAYXPLVUBOIKZGJRFHENMCQ",
     "BMCSRFHLTDENQWAOXPYVUIKZGJ", "XPHKZGJTDSENYVUBMLAOIRFCQW"]
keys=key.split(",")
sequence=[]
for k in keys:
    sequence.append(int(k))
print(sequence)
s_order=[]
print(s[1])
for seq in sequence:
    s_order.append(s[int(seq)-1])
print(s_order)
s_order_decrt=[]
cipher_text_order =['H','C','B','T','S','X','W','C', 'R', 'Q', 'G', 'L', 'E', 'S']
print(cipher_text_order)
for st in range(len(s_order)):
    s2=list(s_order[st])
    s3=[]
    p=0
    for ch in s2:
        p=p+1
        if ch==cipher_text_order[st]:
            for iii in range(len(s2)):
                s3.append(s2[(iii+p-1)%len(s2)])
    print(s3)
ssp= [
    ['H', 'G', 'V', 'S', 'F', 'U', 'W', 'I', 'K', 'P', 'B', 'E', 'L', 'N', 'A', 'C', 'Z', 'D', 'T', 'R', 'X', 'M', 'J',
     'Q', 'O', 'Y'],
    [
        'C', 'P', 'M', 'N', 'Z', 'Q', 'W', 'X', 'Y', 'I', 'H', 'F', 'R', 'L', 'A', 'B', 'E', 'U', 'O', 'T', 'S', 'G', 'J', 'V', 'D', 'K'],
    [
        'B', 'V', 'I', 'Q', 'H', 'K', 'Y', 'P', 'N', 'T', 'C', 'R', 'M', 'O', 'S', 'F', 'E', 'Z', 'W', 'A', 'X', 'J', 'G', 'D', 'L', 'U'],
    [
        'T', 'E', 'Q', 'G', 'Y', 'X', 'P', 'L', 'O', 'C', 'K', 'B', 'D', 'M', 'A', 'I', 'Z', 'V', 'R', 'N', 'S', 'J', 'U', 'W', 'F', 'H'],
    [
        'S', 'L', 'O', 'Q', 'X', 'V', 'E', 'T', 'A', 'M', 'K', 'G', 'H', 'I', 'W', 'P', 'N', 'Y', 'C', 'J', 'B', 'F', 'Z', 'D', 'R', 'U'],
    [
        'X', 'Q', 'Y', 'I', 'Z', 'M', 'J', 'W', 'A', 'O', 'R', 'P', 'L', 'N', 'D', 'V', 'H', 'G', 'F', 'C', 'U', 'K', 'T', 'E', 'B', 'S'],
    [
        'W', 'A', 'T', 'D', 'S', 'R', 'F', 'H', 'E', 'N', 'Y', 'V', 'U', 'B', 'M', 'C', 'O', 'I', 'K', 'Z', 'G', 'J', 'X', 'P', 'L', 'Q'],
    [
        'C', 'E', 'O', 'N', 'J', 'Q', 'G', 'W', 'T', 'H', 'S', 'P', 'Y', 'B', 'X', 'I', 'Z', 'U', 'L', 'V', 'K', 'M', 'R', 'A', 'F', 'D'],
    [
        'R', 'J', 'L', 'X', 'K', 'I', 'S', 'E', 'F', 'A', 'P', 'M', 'Y', 'G', 'H', 'B', 'Q', 'N', 'O', 'Z', 'U', 'T', 'W', 'D', 'C', 'V'],
    [
        'Q', 'W', 'X', 'P', 'H', 'K', 'Z', 'G', 'J', 'T', 'D', 'S', 'E', 'N', 'Y', 'V', 'U', 'B', 'M', 'L', 'A', 'O', 'I', 'R', 'F', 'C'],
    [
        'G', 'O', 'I', 'K', 'F', 'H', 'E', 'N', 'Y', 'V', 'U', 'W', 'A', 'B', 'M', 'C', 'X', 'P', 'L', 'T', 'D', 'S', 'R', 'J', 'Q', 'Z'],
    [
        'L', 'T', 'D', 'E', 'N', 'Q', 'W', 'A', 'O', 'X', 'P', 'Y', 'V', 'U', 'I', 'K', 'Z', 'G', 'J', 'B', 'M', 'C', 'S', 'R', 'F', 'H'],
    [
        'E', 'N', 'Y', 'S', 'R', 'U', 'B', 'M', 'C', 'Q', 'W', 'V', 'J', 'X', 'P', 'L', 'T', 'D', 'A', 'O', 'I', 'K', 'F', 'Z', 'G', 'H'],
    [
        'S', 'W', 'A', 'Y', 'X', 'P', 'L', 'V', 'U', 'B', 'O', 'I', 'K', 'Z', 'G', 'J', 'R', 'F', 'H', 'E', 'N', 'M', 'C', 'Q', 'T', 'D']]

for m in range(len(ssp[1])):
    ssp_flag=[]
    for n in range(len(ssp)):
        ssp_flag.append(ssp[n][m])
    print("".join(ssp_flag))

MMM="XSXSBUGKUADMIN"
print(MMM.lower())