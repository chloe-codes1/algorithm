# ver1) itertools 메모리 초과 뜸...ㅎ_ㅎ  


# from itertools import combinations

# N, K = map(int, input().split())

# degrees = list( map(int, input().split() ))

# options = [ sum(x) for x in list(combinations(degrees, K)) if  ]

# print(max(options))





# ver2) 시간초과...왜이러냐


N, K = map(int, input().split())

degrees = list( map(int, input().split()))

max_sum = 0
for i in range(N -1):
    if degrees[i] >0:
        temp = 0
        for j in range(K):
            temp += degrees[i+j]
    
        if temp > max_sum:
            max_sum = temp

print(max_sum)