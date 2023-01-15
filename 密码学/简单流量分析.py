#!/usr/bin/env python
# coding:utf-8
import base64

packets = open(r"C:/Users/Noky-han/Desktop/m/WP/大三上/简单流量分析/pcap.txt")
f1 = packets.read()
f2 = f1.split("\n")
numlist = []
for sss in f2:
    numlist.append(int(sss))
print(numlist)
for i in range(len(numlist)):
    numlist[i] = chr(numlist[i]-42)
s = ''.join(numlist)
print(base64.b64decode(s))

