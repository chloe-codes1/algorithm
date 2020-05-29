class Node:
    def __init__(self, data,pre, next):
        self.data = data
        self.pre = pre
        self.next = next

def addLast (data):
    global pHead
    global pTail
    if pHead == None: #list가 비어있는 경우
        pHead = Node(data, None,None)
        pTail = pHead
    else: #마지막 노드 추가
        p = Node(data, pTail, None) # 이전 마지막 노드가 앞 노드
        pTail.next = p # 새 노드 연결
        pTail = p  # 새 노드를 마지막 노드로

def addNum(s): # 새 수열을 추가
    global pHead
    global pTail
    p = pHead

    if p==None: #비어있는 경우
        for i in range(N):
            addLast(s[i])
    else:
        while p.next!=None and p.data<=s[0]: # s[0] 보다 큰 수 검색
            p = p.next
        if p.data > s[0]: # 더 큰수를 찾은 경우
            if p.pre == None: #맨 앞인 경우

                else: # 중간

            else: # 맨 마지막에 추가하는 경우



T = int(input())
for t in range(1,T+1):
    N, M= map(int, input().split())
    
    pHead = None
    pTail = None

    for _ in range(M):
        s = list(map(int, input().split()))
    print(s)