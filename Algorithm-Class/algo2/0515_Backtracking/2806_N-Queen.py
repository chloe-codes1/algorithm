def backtrack(idx): #idx = 행
    global N, cnt
    # 최종 상태인지 확인하고, 최종상태이면 해
    if idx == N:
        # 다 찾았음 - 해!
        cnt +=1
        return 
    # 해당 상태에서 선택할 수 있는 후보군 생성
    # Node가 유망한지 확인 : 열 / 상향 대각 / 하향 대각 확인
    for i in range(N):
        # if 열이 유망하고, 대각들이 유망
        if not col[i] and not dia_1[idx +i] and not dia_2[N+i-idx-1]:
            # 모든 후보군에 대해서 다음 상태 실행 
            col[i] = 1
            dia_1[idx+i] = 1
            dia_2[N+i-idx-1] = 1
            # 행을 증가시키기
            backtrack(idx+1)
            # 다시 사용한 것을 없애줌
            col[i] = 0
            dia_1[idx+i] = 0
            dia_2[N+i-idx-1] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())

    # 각 행에는 1개의 Queen만 올 수 있음
    col = [0] * N # 열의 사용 여부를 판단하는 리스트
    # 대각 유망성을 판단할 리스트
    
    # 상향 대각: i와 j의 합이 같음
    dia_1 = [0] * (2*N -1) # (r+c) 로 대각선 번호 매김
    # 하향 대각: i-j 차가 일정
    dia_2 = [0] * (2*N -1) # (N + c -r -1) 로 대각선 번호 매김

    cnt = 0
    backtrack(0)
    print('#{} {}'.format(t,cnt))
