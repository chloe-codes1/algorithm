# ver1) 시간초과나는 재귀 ㅎ_ㅎ ...눈물도 나네...


# T = int(input())

# def score(n,k,s):
#     global options
#     if n == k:
#         options.add(s)
#     else:
#         for i in range(N):
#             if used[i] ==0:
#                 used[i] = 1
#                 score(n+1,k, s+scores[i])
#                 used[i] = 0


# for t in range(1, T+1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     used = [0]*N
#     options = set()

#     for i in range(1,N+1):
#         score(0,i,0)

#     print('#{} {}'.format(t, len(options)+1))
    
    

# ver2) 최대값 기준으로 배열만들기   -> 정답!!
# T = int(input())
 
# for t in range(1, T+1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     used = [0]*10000
#     used[0] = 1
     
#     MAX = 0
#     for s in scores:
#         MAX += s
#         for i in range(MAX, -1, -1):
#             if used[i]:
#                 used[i+s] = 1
#         used[s] = 1
 
#     print('#{} {}'.format(t, used.count(1)))



# ver3) 코드 길이 줄이려고 좀 더 수정 ㅎㅎ

T = int(input())
for t in range(1, T+1):
    N = int(input())
    S = list(map(int, input().split()))
    u = [0]*(10**4)
    MAX = 0
    for s in S:
        MAX += s
        for i in range(MAX, -1, -1):
            if u[i]:
                u[i+s] = 1
        u[s] = 1
    print('#{} {}'.format(t, u.count(1)+1 ))



    
