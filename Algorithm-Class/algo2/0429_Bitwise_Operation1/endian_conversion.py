# Python에서 Endian 변환

import struct #c의 library

num = 27
print(bin(num))
res = struct.pack('i', num)
print('default :', res)

res = struct.pack('> i', num)
print('big endian :', res)

res = struct.pack('< i', num)
print('little endian :', res)

res = struct.pack('! i', num)
print('network :', res)
print('unpack :', struct.unpack('!i',res))