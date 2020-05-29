class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def addList(lst,arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new
    if lst.head is None:
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]: break
            cur = cur.next
        if cur is None: #뒤에
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last

        elif cur.prev is None: #앞에
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else: #중간
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)
             
def printList(lst):
    if lst.head is None: return
    cur = lst.head
    while cur is not None:
        print(cur.data, end=' ')
        cur = next
    print() 

    cur = lst.tail
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.prev
    print()

mylist = LinkedList()

arr = [1,3,5,6,7]
addList(mylist,arr)
printList(addList)