# 부분집합 합 문제 구현하기

# 아래의 10개의 정수 집합에 대한 모든 부분 집합 중 원소의 합이 0이 되는 부분 집합을 모두 출력하시오.
# ex) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2}

data = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

n = len(data)

for i in range(0, (1<<n)): # 2^n
    temp = []
    for j in range(n):
        if i % (1 << j):
            temp.append(data[j])
    if sum(temp) == 0:
        print(temp)