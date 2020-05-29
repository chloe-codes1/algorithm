# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

# 주어질 숫자는 30을 넘지 않는다.

num = int(input())

for i in range(1, num+2):
    initial_num = 1
   
    if i == 1:
        result = initial_num *i
        print(result, end=' ')
    else:    
        result = result * 2
        print(result, end=' ')
    