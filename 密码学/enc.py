

with open(r"C:\Users\Noky-han\Desktop\m\WP\大三上\第一周\enc\enc.txt") as f1:
    cipher_enc_str = f1.read()
    cipher_enc_str = cipher_enc_str.split()
print(cipher_enc_str)
cipher_enc_num = []
for stn in cipher_enc_str:
    if stn == 'ZERO':  # 将字符转换为数字
        cipher_enc_num.append('0')
    else:
        cipher_enc_num.append('1')
cipher_enc_num = ''.join(cipher_enc_num)
print(cipher_enc_num)
cipher_enc = "Li0gLi0uLiAuIC0uLi0gLS4tLiAtIC4uLS4gLSAuLi4uIC4tLS0tIC4uLi4uIC0tLSAuLS0tLSAuLi4gLS0tIC4uLi4uIC4uLSAuLS0uIC4uLi0tIC4tLiAtLS0gLi4uLi4gLiAtLi0uIC4tLiAuLi4tLSAtIC0tLSAtIC0uLi0gLQ=="
cipher_dec = "ALEXCTFTH15O1SO5UP3RO5ECR3TOTXT"
