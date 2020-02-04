# 숫자게임을 좋아하는 새샘이는 서로 다른 7개의 정수 중에서 3개의 정수를 골라 합을 구해서 수를 만들려고 한다.

# 이렇게 만들 수 있는 수 중에서 5번째로 큰 수를 출력하는 프로그램을 작성하라.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 7개의 서로 다른 정수가 공백으로 구분되어 주어진다. 각 정수는 1이상 100이하이다.

 
# [출력]

# 각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 답을 출력한다.




# ver1) 


# import random


# T = int(input())

# for t in range(1, T+1):
#     numbers = list(map(int, input().split()))
#     numbers = sorted(numbers)[2:]
#     options = []
#     for i in range( 6*5*4 ):
#         option = sum(random.sample(numbers,3))
#         if option not in options:
#             options.append(option)
    
#     sorted_options = sorted(options)

#     print('#{} {}'.format(t, sorted_options[-5]))



# ver2)

T = int(input())

for t in range(1, T+1):
    numbers = list(map(int, input().split()))

    options =[0]*6

    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1, 7):
                s = numbers[i] + numbers[j] +numbers[k]
                if s not in options:
                    options[5]= s
                    options = sorted(options, reverse = True)
    
    print('#{} {}'.format(t, options[4]))