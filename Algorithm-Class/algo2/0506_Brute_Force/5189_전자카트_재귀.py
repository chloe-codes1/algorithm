T = int(input())

def f(d, s, t): # d: depth, s: start (출발지점),  t: temp-sum
    global MIN
    if t > MIN: # 가지치기로 시간 복잡도 줄이기! 최솟값을 구하는 문제이므로 최솟값보다 temp-sum이 커지면 바로 return
        return
    if d == N: #depth가 N (관리구역 개수)와 같아졌다는 것은 끝까지 다 봤다는 것이므로 여기에서 최종 합 구하기
        t += field[s][0] #마지막에 다시 첫번째[0]에 위치한 사무실로 돌아올 때의 배터리 사용량 더해주기
        if MIN > t: # 최솟값보다 지금 구한 temp-sum이 작으면,
            MIN = t # 최솟값을 temp-sum으로 교체!
        return
    else:
        for i in range(N): # 1~N 까지 탐색하며
            if not visited[i] and field[s][i]: #아직 방문하지 않은 관리구역이고 (AND) 해당 위치가 0이 아니라면
                visited[i] = 1 # 방문할거니까 방문했다고 표시
                f(d+1,i, t + field[s][i]) #재귀함수 호출 시 depth가 깊어졌으므로 d+1, 현재 방문한 관리구역의 배터리 사용량 temp-sum에 더해주기
                visited[i] = 0 # 다음 경우의 수에서 방문 할 수 있도록 다시 방문하지 않은 것으로 돌려놓긔

for t in range(1, T+1):
    N = int(input())
    field = [ list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N #관리구역 N개에 대한 visited 배열
    MIN = float('inf') #최소 배터리 사용량 구할 것 이므로 비교값보다 큰 float('inf')로 초기화
    visited[0]=1 # 1번은 사무실이고 여기서 출발하니까 visited에 첫번째에 방문 표시  
    f(1, 0, 0) #depth는 1부터 시작하는 것으로 설정! 0으로 하려면 7번째 줄 수정하기 ->  if d== N-1: 으로~
    print('#{} {}'.format(t, MIN))

