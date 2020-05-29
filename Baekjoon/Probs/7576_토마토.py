def bfs(N,M):
    q = [0]*N*M #queue 생성
    visited = [[0]*M for _ in range(N)] #visited 생성
    front = -1#시작점 enqueue
    rear = -1 #시작점 방문 표시
    #시작점 enqueue
    for i in range(N):
        for j in range(M):
            if box[i][j] ==1:
                rear+=1
                q[rear] = (i,j)
                visited[i][j] = 1





# col, row = map(int, input().split())
# box = [list(map( int,input().split())) for _ in range(row)]
# visited = [ [0]*col for _ in range(row)]
# starts = []

# for i in range(row):
#     for j in range(col):
#         if box[i][j] == 1:
#             sr, sc = i,j
#             starts.append((sr,sc))

print(starts)