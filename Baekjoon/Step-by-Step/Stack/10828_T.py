import sys

T = int (sys.stdin.readline())


stack = []

for _ in range(T):
    D = sys.stdin.readline().split()

    if D[0] == 'push':
        stack.append(D[1])
    elif D[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    elif D[0] == 'size':
        print(len(stack))
    elif D[0] == 'pop':
        if len(stack):
            print(stack.pop)
        else:
            print(-1)
    elif D[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)