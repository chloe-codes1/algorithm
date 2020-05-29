data = input()

for i in range(0, len(data), 7):
    cnt = res = 0
    j=i
    while j < len(data) and cnt < 7:
        res = res * 2 + int(data[j])
        cnt += 1
        j +=1
    print(res, end = " ")