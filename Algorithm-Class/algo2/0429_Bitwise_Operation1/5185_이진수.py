T = int(input())

for t in range(1,T+1):
    N, hex_digit = map(str,input().split())
    N = int(N)
    result = ''
    for i in range(N):
        for j in range(3,-1,-1):
            if int(hex_digit[i], 16) & 1 << j:
                result += '1'
            else:
                result += '0'
    print('#{} {}'.format(t, result))
        
        