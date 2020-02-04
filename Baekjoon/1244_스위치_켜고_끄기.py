switches = int(input())

status = list(map(int, input().split()))

students = int(input())

for i in range(students):

    info = list(map(int, input().split()))

    number = info[1]


    if info[0] == 1:
        for i in range(switches):
            if (i+1) % number == 0:
                status[i] = not status[i]
        


    if info[0] == 2:
        
        left = number -2
        right = number

        while True:
            if left < 0 or right > switches -1:
                status[number-1] = not status[number-1]
                break

            if status[left] == status[right]:
                status[left] = not status[left]
                status[right] = not status[right]
                
            else:
                status[number-1] = not status[number-1]
                break

            left -= 1
            right +=1


status = list(map(int, status))

if len(status) <= 20:
    print(*status)
else:
    for i in range(1, switches +1):
        print(status[i], end=' ')

        if i == 20:
            print(sta)
        
