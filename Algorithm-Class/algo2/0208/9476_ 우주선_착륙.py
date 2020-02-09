# 우주선 싸피호는 레이저로 착륙할 곳의 높이를 측정해 안정적인 착륙장소를 정한다. 측정한 정보는 N개 행과 M개 열의 영역으로 구분되며, 우주선이 착륙하기 위해서는 최소 3x3 크기의 영역이 조건을 만족해야만 한다.

# 1. 본체가 위치하는 칸을 중심으로 주변 8칸중 가장 높은 곳과 낮은 곳의 차이 d가 K 이하(d<=K)여야 한다.

# 2. 본체가 위치한 칸은 주변 8칸 중 가장 낮은 칸과 같거나 높고, 높이 차이 e가 H 이하(e<=H)여야 한다.

# 만약 K=3, H=2 인 경우의 다음과 같은 지형에 착륙할 수 있다.

# 1

# 2

# 3

# 4

# 2

# 4

# 3

# 2

# 1

# 다음과 같은 지형에는 착륙할 수 없다.

# 1

# 2

# 3

# 4

# 3

# 5

# 3

# 2

# 1

 

# 어떤 구역에 대한 높이 정보가 주어질 때, 우주선 본체가 위치할 수 있는 칸의 개수를 알아내는 프로그램을 작성하시오.
 
# 입력

# 검토해야할 구역의 개수 T가 첫 줄에 주어진다. 다음 줄부터 첫 줄에 구역의 크기 N, M, 높이제한 K, H가 차례로 주어지고, 다음 줄부터 N줄에 걸쳐, M개 씩의 높이 정보 Aij가 제공된다.

# 3<=N, M<=100, 0

# 출력

# #과 1번부터 시작하는 구역번호, 우주선 본체가 착륙할 수 있는 칸의 수를 출력한다. 착륙할 수 있는 칸이 없는 경우 0을 출력한다.


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]



T = int(input())

for t in range(1, T+1):

    row, col, K, H = map(int, input().split())

    area = [ list(map (int, input().split())) for _ in range(row) ]

    count = 0

    for i in range(1, row-1):
        for j in range(1, col-1):
            center = area[i][j]

            max_height = 0
            min_height = 100000

            for k in range(8):
                temp_row = i + dr[k]
                temp_col = j + dc[k]
                position = area[temp_row][temp_col]
                
                if position > max_height:
                    max_height = position

                if position < min_height:
                    min_height = position
            

            if max_height - min_height <= K:
                if center >= min_height:
                    if center - min_height <=H:
                        count+= 1

    print('#{} {}'.format(t, count))


                

