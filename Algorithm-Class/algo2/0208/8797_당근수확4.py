# 영준이의 새로운 당근밭은 NxN개의 구역으로 구성되어 있는데, 각 구역에 접근하기 쉽도록 다음과 같이 대각선인 구역을 연결해 통로를 만들려고 합니다. 통로를 제외한 4개의 영역이 오른쪽 그림과 같다고 할 때, 각 구역의 당근 수확량 중 최대와 최소인 경우의 차를 구하는 프로그램을 만드세요.



# 구역별로 수확할 당근의 개수가 주어집니다.
# N은 항상 홀수입니다.

# 입력

# 첫 줄에 테스트케이스 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과, 다음 줄부터 N개씩 N줄에 걸쳐 구역별로 수확할 당근의 개수 C가 제공됩니다.

# 1<=T<=50, 5<=N<20, 0<=C<=10

 

# 출력

# 테스트케이스별로 각 줄에 #과 테스트케이스 번호, 구역별 수확량 합계의 최대와 최소값의 차이를 출력합니다.



def rotate(array):
    N = len(array)
    result = [[0] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            result[col][N-1-row] = array[row][col]
    return result


T = int(input())
for t in range(1, T+1):
    size = int(input())
    field = [list(map(int, input().split())) for _ in range(size) ]

    max_harvest = 0
    min_harvest = 10000

    for _ in range(4):

        harvest = 0
        k = 0
        for i in range(size//2):
            for j in range(1 + k, size-k):
                harvest += field[i][j]
            
            k += 1

        if harvest > max_harvest:
            max_harvest = harvest
        if harvest < min_harvest:
            min_harvest = harvest

        field = rotate(field)

    print('#{} {}'.format(t,max_harvest - min_harvest))

            