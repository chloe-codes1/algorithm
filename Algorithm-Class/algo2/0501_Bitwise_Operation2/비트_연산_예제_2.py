# 16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit 씩 묶어 십진수로 변환하여 출력해보자


"""
0f97a3
000011111001011110100011
7 101 116 3
"""


def convert(num):
    if num.isdigit():
        num = int(num)
    else:
        num = 10 + ord(num.upper()) - ord('A')

    # ver1)
    temp = ''
    for i in range(3, -1, -1):
        temp  += '1' if (num & (1 <<i)) else '0'

    # ver2_
    t=[0]*4
    for j in range(4):
        t[3-j] = str((num >> j) & 1)
    print(''.join(t))
    return temp

hex_num = input()
binary = ''
for i in range(len(hex_num)):
    tmp = convert(hex_num[i]) 
    binary += tmp
print(binary)

for i in range(0, len(binary), 7):
    dec=0
    try:
        for j in range(7):
            dec = dec*2 + int(binary[i+j])
    except:
        pass
    print(dec, end= " ")