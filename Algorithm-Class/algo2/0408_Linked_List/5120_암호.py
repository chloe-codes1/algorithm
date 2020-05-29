T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())     
    pw = list(map(int, input().split()))
    idx = 0
    for _ in range(1, K+1):
        idx += M
        if idx < N:
            pw.insert(idx, pw[idx-1] + pw[idx])
        else:
            if idx % N:
                idx = idx % N
                pw.insert(idx, pw[idx-1] + pw[idx])
            else:
                pw.insert(idx, pw[-1] + pw[0])
        N += 1
    print('#{}'.format(t), *pw[-1:-11:-1])