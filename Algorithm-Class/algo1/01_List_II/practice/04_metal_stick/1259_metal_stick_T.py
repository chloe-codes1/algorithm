import sys

sys.stdin = open('input.txt')

## 전제 조건
## 1. 같은 나사는 없다
## 2. 모든 나사는 이어진다


T = int (input())

for t in range(1, T+1):
    N = int(input())

    d = list(map(int, input().split()))

    pipes = [ [d[i], d[i+1]] for i in range(0, N*2, 2)]

    connected = pipes.pop()
    
    # pipes가 비면 False라서 break
    while pipes:
        for i in range(len(pipes)):

            #앞으로 연결
            if pipes[i][0] == connected[-1]:
                connected += pipes.pop(i)  # + 는 extend와 똑같음
                break
            #뒤로 연결
            if pipes[i][-1] == connected[0]:
                connected = pipes.pop(i) + connected
                break

    print('#{}'.format(t), *connected)