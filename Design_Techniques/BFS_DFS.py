graph = {
'A': ['B'],
'B': ['A', 'C', 'H'],
'C': ['B', 'D'],
'D': ['C', 'E', 'G'],
'E': ['D', 'F'],
'F': ['E'],
'G': ['C'],
'H': ['B', 'I', 'J', 'M'],
'I': ['H'],
'J': ['H', 'K'],
'K': ['J', 'L'],
'L': ['K'],
'M': ['H']
}


def BFS(graph, start_node):
    #방문했던 노드 목록 저장
    visited = {}  
    # -> list로 하면 33번째 줄 if node not in visited: 에서 시간 복잡도가 O(n)이 소요되므로 dictionary 사용
    
    #다음으로 방문할 노드 목록
    queue =  []

    queue.append(start_node)

    #큐의 목록이 바닥날때까지(더 이상 방문할 노드가 없을 때까지) loop를 돌려준다.
    while queue:
        #큐의 맨 앞에있는 노드를 꺼내온다.
        node = queue.pop(0)

        #해당 노드가 아직 방문 리스트에 없다면,
        if node not in visited:

            #방문 리스트에 추가해주고,
            visited[node] = True

            #해당 노드의 자식 노드들을 큐에 추가해준다.
            queue.extend(graph[node])

    return visited


def DFS(graph, start_node):
    visited = {}
    stack = []

    stack.append(start_node)

    while stack:

        #pop()은 마지막 index를 가져오므로 stack과 동일하게 동작
        node = stack.pop()
        if node not in visited:
            visited[node] =True
            stack.extend(graph[node])

    return visited



print(BFS(graph, 'A'))
print('-'*10)
print(DFS(graph, 'A'))