# BFS / DFS



### BFS ( = Breath First Search, 너비 우선 탐색 ) 

> 한 단계씩 나아가면서 해당 노드와 같은 레벨에 있는 형제 노드들을 먼저 순회하는 방식



- 인접한 node들을 탐색 후, 차례로 너비 우선 탐색을 진행해야 하므로 FIFO Structure 인 Queue 활용

<br/>

```python
def BFS(G, v): #graph G, 탐색 시작점 v
    visited = [0]*n #n == node 개수
    queue = [] #queue 생성
    queue.append(v) #시작점 v를 queue에 넣기
    while queue: #queue가 비어있지 않은 동안
        t = queue.pop(0) #queue의 첫번째 원소 반환
        if not visited[t]: #방문되지 않은 곳이라면
            visited[t] = True #방문한 것으로 표시
            visit(t)
        for i in G[t]: # t와 연결된 모든 선에 대해
            if not visited[i]: #방문되지 않은 곳이라면
                queue.append(i) #queue에 넣기
```



<br/>

<br/>



### DFS ( = Depth First Search, 깊이 우선 탐색)

> 한 노드의 자식을 타고 끝까지 순회한 다음에, 다시 돌아와서 다른 형제의 자식을 타고 내려가며 순회하는 방식

- 가장 마지막에 만났던 갈림길의 node로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 LIFO Structure인 Stack 활용

<br/>