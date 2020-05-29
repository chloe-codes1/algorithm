# 숫자 N은 아래와 같다.

# N=2a x 3b x 5c x 7d x 11e

# N이 주어질 때 a, b, c, d, e 를 출력하라.


# [제약 사항]

# N은 2 이상 10,000,000 이하이다.


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.


# [출력]

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)



T = int(input())

for i in range(1, T+1):
    N = int(input())
    a,b,c,d,e = [0] *5
    idx =2
    
    while N!=1:

        if N%idx == 0:
            N/=idx 
            if idx == 2:
                a+=1
            elif idx == 3:
                b+=1
            elif idx == 5:
                c+=1
            elif idx == 7:
                d+=1
            elif idx == 11:
                e+=1

            idx =2
        else:
            idx +=1

    print('#{0} {1} {2} {3} {4} {5}'.format(i,a,b,c,d,e))    