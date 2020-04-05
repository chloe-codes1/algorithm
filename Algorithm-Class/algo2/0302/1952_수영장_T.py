T = int(input())

def f(n,s, d, m, m3):
    global minV
    if n > 12:
        if minV > s:
            minV = s
    else:
        f(n+1, d*table[n] + s, d,m,m3 )
        f(n+1, s+m, d,m,m3)
        f(n+3, s )
    





for t in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    table = [0] + list(map(int, input().split()))
    minV = y
    f(1,0,d,m,m3)
    print('#{} {}'.format(t, minV))











# import copy


# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
    
#     numbers = list(map(int,input().split()))

#     temp = [0]*10

#     for _ in range(N):
#         for i in range(10):
#             if i == 0 or i==9:
#                 if numbers[i] <= 0:
#                     temp[i] += numbers[i][1:]
#                 else:
#                     temp[i] += '-'+ numbers[i]

#                 if abs(int(numbers[i])) >=10:
#                         if i == 0:
#                             temp[i+1] += str(abs(int(numbers[i]))//2)
#                             temp[i] += str(abs(int(numbers[i]))//2)
#                         if i == 9:
#                             temp[i-1] += str(-abs(int(numbers[i]))//2)
#                             temp[i] +=  str(abs(int(numbers[i]))//2)
#             else:
#                 if abs(int(numbers[i])) >=10:
#                     temp[i-1] += str(int(numbers[i-1]) - abs(int(numbers[i]))//2)
#                     temp[i+1] += str(int(numbers[i+1]) + abs(int(numbers[i]))//2)
#                     temp[i] = '0'
#                 else:
#                     if numbers[i][0] == '-':
#                         temp[i-1] += str(int(numbers[i-1]) + int(numbers[i]))
#                         temp[i] = '0'
#                     else:
#                         temp[i+1] += str(int(numbers[i]) + int(numbers[i+1]))
#                         temp[i] = '0'
#             numbers = copy.deepcopy(temp)
#             temp = [0]*10


#         print(numbers) 