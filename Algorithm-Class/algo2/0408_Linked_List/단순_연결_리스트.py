class Node:
    def __init__(self, d=0, n=Node):
        self.data = d # 정수 값
        self.next = n # 다음 node 주소

class LinkedList:
    def __init__(self):
        self.head = None  # 첫 번째 노드
        self.tail = None  # 마지막 노드
        self.size = 0     # 노드의 수

mylist = LinkedList()

def printList(lst): # list: LinkedList 객체
    cur =lst.head

    print(lst.size, '[', end='')
    while cur.next is not None:
        print(cur.data, end=' ')
        cur = cur.next
    print(']')


def insertLast(lst, new): # new: 새로 추가할 node 객체
    # 빈 list일 경우
    if lst.head is None:
        lst.head = new
    else:
        lst.tail.next = new
        lst.tail = new
       
    lst.size += 1

def deleteLast(lst):
    if lst.head is None: return

    pre, cur = None, lst.head
    while cur.next is not None:
        pre = cur
        cur = cur.next

    if pre is None:
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre
    lst.size -=1

def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new
    lst.size += 1

def deleteFirst(lst):
    if lst.head is None: return

    # Node가 1개일 경우 주의한다
    lst.head = lst.head.next
    if lst.head is None:
        lst.tail = None

    lst.size -= 1

def insertAt(lst, idx, new): #idx: index 값
    # 빈 리스트일 경우, idx == 0
    if lst.head is None or idx ==0:
        insertFirst(lst, new)
    elif:
        # 중간에 추가하는 경우
        insertLast(lst,ne)
    else:
        pre, cur = None, lst.head
        pre = cur
        cur = cur.next 

for i in range(5):
    insertFirst(mylist, Node(i))
    printList(mylist)




# while mylist.size:
#     deleteLast(mylist)
#     printList(mylist)