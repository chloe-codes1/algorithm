

import sys

sys.stdin = open('input.txt')


def check(n):
    n, r = n // 10, n % 10

    digits = []
    while n!=0:
        if n % 10 > r:
            returnFalse

        n, r = n//10, n%10
    
    digits.append(r)


    return True


T = int(input())

for t n range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = -1

    for i in range(N):
        for j in range(i+1, N):
            num = numbers[i] *numbers[j]
            if result < num:
                # check 함수를 통과 하면,
                if check(num):
                    result = num

    print('#{} {}'.format(t, result))   