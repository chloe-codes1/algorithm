T = int(input())

for t in range(1, T+1):
    stack = []
    D = input()
    for c in D:
        if stack:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)


    print('#{} {}'.format(t, len(stack)))

