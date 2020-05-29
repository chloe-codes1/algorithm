
def rotate(a):
    N = len(a)

    result = [ [0]*N for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            result[j][N-i-1] = a[i][j]

    return result

a = [ [1,2,3,], ['a','b','c'], [ 0,0,0]]


print(rotate(a))
