from itertools import combinations

T = int(input())

for t in range(1, T+1):
    result = 100000
    N = int(input())
    ingredients = [ list(map(int, input().split())) for _ in range(N)]

    for c1 in combinations(range(N), N//2):
        c2 = [ i for i in range(N) if i not in c1]
        s1,s2 = 0,0
        for row in range(N//2-1):
            for col in range(row+1, N//2):
                s1 += ingredients[c1[row]][c1[col]] + ingredients[c1[col]][c1[row]]
                s2 += ingredients[c2[row]][c2[col]] + ingredients[c2[col]][c2[row]]
        temp = abs(s1-s2)
        if temp < result:
            result = temp

    print('#{} {}'.format(t, result))