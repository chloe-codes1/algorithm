
import sys
sys.stdin = open('input.txt')


def pascal(x,y):
    if y == 0 or x==y:
        return 1
    elif y < 0 or x <y:
        return 0
    
    return pascal(x-1, y-1) + pascal(x-1, y)




T = int(input())

for t in range(1, T+1):

    print('#{} '.format(t))
    N = int(input())    
    for i in range(N):
        for j in range(i+1):
            print(pascal(i,j), end=' ')
        print()


