# 13  
# = 정점의 개수  / 간선 수 = V-1 =12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

V = int(input())
E = V -1
arr = list(map(int, input().split()))

L = [0]*(V+1) #왼쪽
R = [0]*(V+1) #오른쪽
P = [0]*(V+1) #부모

for i in range(0, E*2, 2):
    parent, child = arr[i], arr[i+1]
    if L[parent]:
        R[parent] = child
    else:
        L[parent] = child
    P[child] = parent

def inorder(v): # v = 방문하는 노드 번호
    if v == 0:
        return
    # 전위 순회 위치
    inorder(L[v])
    # 중위 순회 위치(왼쪽 자식에 대한 함수 호출이 끝나고 v에 대해 하고싶은걸 하는 것!)
    print(v, end=' ')
    inorder(R[v])
    # 후위 순회 위치

inorder(1)
