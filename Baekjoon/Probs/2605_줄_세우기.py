
N = int(input())

students = [ s for s in range(1, N+1)]
selected = list( map(int, input().split()))


ordered = [1]

for i in range(1, N):
    ordered.insert(i - selected[i],students[i])


print(*ordered)





