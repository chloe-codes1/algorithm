# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오. 두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.

# 예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.



# 노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

# 어떤 노드는 자신으로 되돌아오는 경로가 있을 수 있다.

 

# 입력

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

# 다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000

# 테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.

# E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.

 

# 출력

# #과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.



T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    infos = [ list( input().split()) for _ in range(E) ]
    starts = [ infos[i][0] for i in range(E)]

    start, end = input().split()

    visited = []
    result = 1

    while True:

        for i in range(E):
            if infos[i][0] == start:
                start = infos[i][1]
                visited.append(infos[i])
                E -= 1
                infos.pop(i)
                break
        if start == end:
            break
    
        
        if start not in starts:
            if visited:
                start = visited[-1][0]
                visited.pop()
                starts.remove(start)

            else:
                result = 0
                break

    print('#{} {}'.format(t, result))