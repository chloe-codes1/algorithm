def bfs(G,v): # 그래프 G, 탐색 시작점 v
    visited = [0]*N # 정점의 개수 N
    queue = [] # queue 생성 
    queue.append(v) #시작점 v를 queue에 삽입
    visited[v] = True
    while queue: # queue가 비어있지 않은 경우
        t = queue.pop(0) # queue의 첫번째 원소 반환
        visited(t)
        for i in G[t]:  # t와 연결된 모든 선에 대해
            if not visited[i]: #방문되지 않은 곳
                queue.append(i) # queue에 넣기
                visited[i] = True