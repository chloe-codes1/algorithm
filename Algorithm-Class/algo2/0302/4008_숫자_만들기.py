T =  int(input())

def f(n, total):
    global min_val, max_val
    if n >= N:
        max_val = max(max_val,total)
        min_val = min(min_val,total)
        return
    else:
        for i in range(4):
            if operators[i] > 0:
                operators[i] -= 1

                if i == 0:
                    f(n+1, total + nums[n])
                elif i ==1:
                    f(n+1, total - nums[n])
                elif i ==2:
                    f(n+1, total * nums[n])
                elif i ==3:
                    f(n+1, int(total/nums[n]))

                operators[i] +=1

for t in range(1, T+1):
    N = int(input())
    operators = list(map(int, input().split()))
    nums = list(map(int,input().split()))

    min_val = 10000000
    max_val = -10000000

    f(1, nums[0])
       
    print('#{} {}'.format(t, max_val - min_val))