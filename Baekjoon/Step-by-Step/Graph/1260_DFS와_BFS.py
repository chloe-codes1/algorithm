# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.


def DFS(matrix, vertex, start):
    stack = []
    visited = [ 0 for _ in range(vertex+1)]
    result = []
    stack.append(start)
    visited[start] = 1
    result.append(start)

    while stack:
        temp = start
        for spot in matrix[start]:
            if not visited[spot]:
                stack.append(spot)
                visited[spot] = 1
                start = spot
                result.append(start)
                break
        else:
            if temp == start:
                stack.pop()
    
    return result



def BFS(matrix, vertex, start):
    queue = []
    result = []
    visited = [ 0 for _ in range(vertex +1)]
    queue.append(start)
    result.append(start)

    while queue:
        temp = queue.pop(0)
        if not visited[temp]:
            visited[temp] = True
        
        for spot in matrix[temp]:
            if not visited[spot]:
                queue.append(spot)
                result.append(spot)
                visited[spot] = True

    
    return result









vertex, edge, start = map(int, input().split())

matrix = [ [] for _ in range(vertex+1) ]

for _ in range(edge):
    f, t = map(int, input().split())

    matrix[f].append(t)
    matrix[t].append(f)


print(DFS(matrix,vertex,start))
print(BFS(matrix,vertex,start))