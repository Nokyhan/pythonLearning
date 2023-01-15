from string import ascii_uppercase, ascii_lowercase, digits
from Crypto.Util.number import long_to_bytes


def solve():
    with open('D:/EdgeDownload/1a351e90fb2b476a929d1e2666d7c511', 'r') as file:
        f = file.read()
    lc = f.split('\n')[:-1]  # split最后一个字符为空，因此要去到倒数第二个
    # base就是对应的64个字符
    base = ascii_uppercase + ascii_lowercase + digits + '+/'

    re2 = []
    for code in lc:
        if '==' in code:  # 如果是编码一个字节
            re2.append(bin(base.find(code[-3]))[2:].rjust(6, '0')[2:])
        elif '=' in code:  # 如果是编码两个字节
            re2.append(bin(base.find(code[-2]))[2:].rjust(6, '0')[4:])
    ret = ''.join(re2)
    return long_to_bytes(int(ret[:ret.rfind('1') + 1], 2), 2).decode()


if __name__ == '__main__':
    print(solve())
