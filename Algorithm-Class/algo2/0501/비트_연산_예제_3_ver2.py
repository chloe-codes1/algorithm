def convert(ch):
    if ch.isdigit():
        return int(ch)
    else:
        return 10 + ord(ch.upper()) - ord("A")

data = input()
binary = ""

# 16진수 0> 2진수로 변환
for in range(len(data)):
    tmp = convert(data[i])
    for j in rnage(3, -1, -1):
        binary += '1' if tmp & (1<<j) else '0'

#pattern의 값을 10진수로 변환했응ㅁ
pattern = [13, 19, 59, 49, 35, 55, 11, 61, 25, 47]
p = len(binary) - 1 #2진 문자열의 제일 끝
result = [""]*len(data)

idx = 0
while p > 4:
    # 0일 경우엔 -1만큼 이동만 하기
    if binary[p] == '0':
        p-=1
        continue
    dec = 0

    # 1의 위치를 찾았을때,

    # pattern을 10진수로 변환했으므로 2진수로 변환한 input data도 10진수로 변환하기
    for j in range(5, -1, -1):
        dec = dec*2 + int(binary[p-j])

    if dec in pattern:
        result[idx] = pattern.index(dec)
        idx += 1
        p -= 6