import sys

V, edge = map(int, input().split())

M = [ [0]*V for _ in range(V)  ]

# 인접리스트 ver1)
G = {node: [] for node in range(V)}

# 인접리스트 ver2)
# : index 자체가 node의 번호를 의미하는 인접 리스트  -> 숫자일때만 가능!
# G = [[] for _ in range(V)]


# Edge들만 저장되어있는 list
F = []



for e in range(edge):
    f, t = map(int, input().split())  # from, to

    # 1. 인접 행렬 [[]]

    M[f][t] = M[t][f] = 1 #다중할당  -> 친구관계는 양방향이니까!

    # 2. 인접 리스트 { f: [t1,t2]}

    G[f].append(t)
    G[t].append(f)

    # 3. Edge list    - 역시 양방향으로 만들어줌
    F.append([f,t])
    F.append([t,f])

for i in range(len(F)):
    for j in range(len(F)):
        A, B  = F[i]
        C, D = F[j]

        if A == B or A == C or A==D or B==C or B==D or C ==D:
            continue

        if not M[B][C]:
            continue

        for E in G[D]:
            if E == A or E == B or E==C or E==D:
                continue
            print(1)
            sys.exit(0) #종료시켜서 아예 빠져나가기


# for문을 다 통과하고 없으면 print
else:
    print(0)


