"""
Prob)
16진수 문자로 이루어진 1차 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오.
암호는 연속되어있다.

암호 비트 패턴
0 - 001101
1 - 010011
2 - 111011
3 - 110001
4 - 100011
5 - 110111
6 - 001011
7 - 111101
8 - 011001
9 - 101111
"""

# Solution) 패턴 다 1로 끝남 -> 뒤에서부터 읽어서 1로 끝나는 위치부터 앞으로 6자리를 읽어서 값 찾기

arr = '0269FAC9A0'

arr = arr.replace('0', '0000')
arr = arr.replace('1', '0001')
arr = arr.replace('2', '0010')
arr = arr.replace('3', '0011')
arr = arr.replace('4', '0100')
arr = arr.replace('5', '0101')
arr = arr.replace('6', '0110')
arr = arr.replace('7', '0111')
arr = arr.replace('8', '1000')
arr = arr.replace('9', '1001')
arr = arr.replace('A', '1010')
arr = arr.replace('B', '1011')
arr = arr.replace('C', '1100')
arr = arr.replace('D', '1101')
arr = arr.replace('E', '1110')
arr = arr.replace('F', '1111')


patt = ['001101','010011', '111011', '110001',
        '100011', '110111', '001011', '111101',
        '011001', '101111']

# replace 결과, arr에는 2진수로 변환된 문자열이 저장되어 있음

# 패턴이 있는지 확인하기
for i in range(len(arr) - 6):
    if arr[i: i+6] in patt:
        x = patt.index(arr[i: i+6])
        break

print(arr)
for i in range(arr.index(patt[x]), len(arr) -6, 6):
    print(patt.index(arr[i: i+6]), end= ' ')
