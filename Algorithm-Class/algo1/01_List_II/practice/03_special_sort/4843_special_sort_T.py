import sys

sys.stdin = open('input.txt')


T = int(input())

for t in range(1, T+1):
    N = int(input())

    d = sorted(list(map(int, input().split())))

    # slicing으로 뒤에 반만 뒤집기
    r = d[-5:][::-1]

    print('#{}'.format(t), end= ' ')

    for i, j in zip(r, d[:5]):
        print(i, end=' ')
        print(j, end=' ')
    
    print()