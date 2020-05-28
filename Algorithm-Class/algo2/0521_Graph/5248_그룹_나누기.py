
def find_set(x):
    if parent[x] == x:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y
    if rank[x] == rank[y]:
        rank[x] += 1

T = int(input())
for test_case in range(1, 1+ T):
    N, M = map(int, input().split())
    preference = list(map(int, input().split()))
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    for i in range(M):
        union(preference[2 * i], preference[2 * i + 1])
    result = set()
    for j in range(1, 1 + N):
        result.add(find_set(j))
    print('#{} {}'.format(test_case, len(result)))
