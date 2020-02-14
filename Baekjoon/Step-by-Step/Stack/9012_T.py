import sys

T = int(sys.stdin.readline())


#ver1) stack 활용

for _ in range(T):
    D = sys.stdin.readline().strip()
    stack = []
    for p in D:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) ==0:
            print('YES')
        else:
            print('NO')



#ver2) stack이 아니라 변수 길이만 기억하는 counting 방법

for _ in range(T):
    D = sys.stdin.readline().strip()
    stack = 0
    for p in D:
        if p == '(':
            stack +=1
        else:
            if stack != 0:
                stack -= 1
            else:
                print('NO')
                break
    else:
        if stack ==0:
            print('YES')
        else:
            print('NO')
        
