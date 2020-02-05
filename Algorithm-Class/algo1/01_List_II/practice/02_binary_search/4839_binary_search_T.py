

import sys
sys.stdin = open('input.txt')

T = int(input())

# index가 even 일 때, 중간 지점 설정을 위해 일관된 기준이 필요함
#   => 보통은 몫 (//) 을 구해서 사용!


def find (total, target):
    l = 1
    r = total
    m = int((l+r)/2)  #int()도 // 몫 연산자와 같이 부동소수점 이하를 버려줌

    cnt = 1

    #중간값과 찾는 값이 같아질 때 까지 반복
    while m != target:
        if m < target:
            l = m
        else:
            r = m

        m = int((l+r)/2)
        cnt +=1

    return cnt




for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    A = find(P, Pa)
    B = find(P, Pb)

    result = '0'
    if A < B:
        result = 'A'
    elif A > B:
        result = 'B'

    
    print('#{} {}'.format(t, result))