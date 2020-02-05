
#1. 10 x 10 격자 생성
#2.
#3. 겹쳐진 구간의 개수 출력(cnt)




import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    cnt = 0
    tile = [[0]*10 for _ in range(10) ]
 
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # x축의 범위
        for i in range(r1, r2 +1):
            # y축의 범위
            for j in range(c1, c2 +1):
                tile[i][j] += color
                if tile[i][j] == 3:
                    cnt += 1

    print('#{} {}'.format(t,cnt))