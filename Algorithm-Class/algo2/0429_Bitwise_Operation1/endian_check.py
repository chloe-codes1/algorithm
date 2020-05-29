# Endian 확인하기

# ver1)

n = 0x00111111

if n&0xff: #0xff = 11111111 이다!
    print("little endian")
else:
    print("big endian")

print('-'*20)

#ver2) python sys library 활용

import sys
if sys.byteorder == "little":
    print("Little endian platform")
else:
    print("Big endian platform")
