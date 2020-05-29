def enqueue(n):
    global rear

    if rear == len(q)-1:
        print('full!')
    else:
        rear +=1
        q[rear]= n


q = [0]*3
front = -1
rear = -1

rear += 1 #enq(1)
q[rear] = 1
rear += 1 #enq(2)
q[rear] = 2
rear += 1 #enq(3)
q[rear] = 3

while front != rear:
    front += 1
    print(q[front])

print('-'*10)

Q = []
Q.append(1) # enqueue(1)
print(Q.pop(0)) #dequeue()


q1 = []
x=2
y=5
q1.append((x,y))

i, j = q1.pop(0)

print(i,j)