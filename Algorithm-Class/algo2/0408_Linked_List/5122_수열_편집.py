T = int(input())

for t in range(1, T+1):
    N, M, L = map(int, input().split())
    base = list(map(int, input().split()))
    for _ in range(M):
        editor = list(input().split())
        order = editor[0]
        if order == 'I':
            base.insert(int(editor[1]), int(editor[2]))
        elif order == 'D':
            base.pop(int(editor[1]))
        elif order == 'C':
            base[int(editor[1])] = int(editor[2])
    print('#{} {}'.format(t, base[L] if len(base) > L else -1 ))
    