

T = int(input())
for t in range(1, T+1):
    N = int(input())

    options = list(map(int, input().split()))
    

    result = -1
    for i in range(N):
        for j in range(i+1, N):
            candidate = str(options[i] * options[j]) 
                
            found = True
            for c in range(len(candidate) -1):
                if int(candidate[c]) > int(candidate[c+1]):
                    found = False
                    break
                
            if found and result < int(candidate):
                result = int(candidate)


    print('#{} {}'.format(t, result))