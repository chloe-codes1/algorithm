"""
[상태]
x = (현재시간 - 번식시간)//생명력

x < 1: 비활성
x < 2: 활성
x >= 2: 죽은 세포
x > 1: 번식

[고려할 공간의 크기]
초기 영역이 N*M 이 최대 50*50
배양 시간 K는 300이하
무한한 크기가 아니라 배양시간 동안 사방으로 번서ㅣㄱ할 크기만 필요
=> N*M 을 (N+K)*(M+K)중심부로 이동하고 시작
=> (K//2 - t//2, K//2 - t//2) 부터 (N-1 + K//2 + t//2, M-1 + K//2 + t//2) 까지

"""

def f(N,M,K,org):
    d = K//2
    ts = [[-1]*(M+K) for _ in range(N+K)] # timestamp - 부착시간
    cell = [[0]*(M+K) for _ in range(N+K)] # 줄기세포 - 생명력
    for i in range(N):
        for j in range(M):
            cell[i+d][j+d] = org[i][j] # 중간으로 옮김
            if org[i][j] != 0: # 초기에 세포가 있으면 timestamp 0으로
                ts[i+d][j+d] = 0

    for h in range(1, K+1): # 배양시간별 각 칸의 상태 정의
        for i in range(d-h//2, N+d+h//2): # 시간이 지날수록 확인 영역 확장
            for j in range(d-h//2, M+d+h//2):
                tmp = [] # 주변의 활성세포 생명력 리스트
                if not cell[i][j]: # 아직 세포가 없으면,
                    for k in range(4): # 주변 확인 
                        ni = i+di[k]
                        nj = j+dj[k]
                        if 0 <= ni < N+K and 0 <= nj < M+K:
                            if cell[ni][nj] >0 and (h-ts[ni][nj])/cell[ni][nj] > 1: # 활성 세포가 있으면,
                                tmp.append(cell[ni][nj]) # 생명력 리스트 만듦
                    if len(tmp) >0: 
                        cell[i][j] = max(tmp) #세포 생성
                        ts[i][j] = h # 세포 생성 시간 기록

    cnt = 0
    for i in range(N+K):
        for j in range(M+K):
            if cell[i][j] > 0 and (K-ts[i][j]) // cell[i][j] <2:
                cnt +=1
    return cnt

di = [0,1,0,-1]
dj = [1,0,-1,0]

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    org = [ list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(t,f(N,M,K,org)))