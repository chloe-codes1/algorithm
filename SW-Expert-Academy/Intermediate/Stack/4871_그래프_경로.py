# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.

# 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
 

# 예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
 

 

# 노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

 
 

# [입력]
 

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
 

# 다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
 

# 테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
 

# E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

 

# [출력]
 

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.



# ver 1) 산으로 가고있음

# T = int(input())
# for t in range(1, T+1):
#     nodes, lines = map(int, input().split())

#     infos = {}

#     for n in range(lines):
#         start, end = input().split()

#         if start not in infos.keys():
#             infos.update({start : end })
#         else:
#             infos[start] += end

#         # print(infos)

#     departure, arrival = input().split()

#     print('나오니? ',infos[departure])
    


# ver 2)

T = int(input())
for t in range(1, T+1):
    nodes, lines = map(int, input().split())

    infos = [list(input().split()) for _ in range(lines) ]

    starts = [ infos[i][0] for i in range(lines) ]

    start, end = input().split()

    temp = []
    result = 1
    while True:

        for i in range(lines):
            if start == infos[i][0]:
                start = infos[i][1]
                lines -= 1
                temp.append(infos[i])
                infos.pop(i)
                break

        if start == end:
            break

        if start not in starts:
            if temp:
                start = temp[-1][0]
                temp.pop()
                starts.remove(start)

            else:
                result = 0
                break

    print('#{} {}'.format(t, result))
