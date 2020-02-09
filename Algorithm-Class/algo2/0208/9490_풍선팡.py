# 종이 꽃가루가 들어있는 풍선이 M개씩 N개의 줄에 붙어있고, 어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임이 있다.

# 예를 들어 풍선에 든 꽃가루가 1개씩일 때, 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.

 

# NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력하는 프로그램을 만드시오.

# (3<=N, M<=100)

 

# 입력

# 첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M, 이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.

 

# 출력

# #과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다.

dr = [-1, 0 ,1, 0]
dc = [0, -1, 0, 1]


T = int(input())

for t in range(1, T+1):
    row, col = map(int, input().split())

    balloons = [ [0] + list( map(int, input().split())) + [0] for _ in range(row) ]
    balloons.insert(0, [0]*(col+2) )
    balloons.append([0] *(col+2))

    max_s = 0

    for i in range(1, row+1):
        for j in range(1, col+1):
            center = balloons[i][j]
            s = center
            for k in range(4):
                p =0
                temp_row = i + dr[k]
                temp_col = j + dc[k]
                position = balloons[temp_row][temp_col]

                while position != 0:
                    if p >= center:
                        break
                    s += position
                    p += 1
                    temp_row += dr[k]
                    temp_col += dc[k]
                    position = balloons[temp_row][temp_col]

                if max_s < s:
                    max_s = s

    print('#{} {}'.format(t,max_s))    
