def getNumber(x,y):

    point = 1 + ((x+y-1)*(x+y))//2 -y

    return point


def getPoint(number):

    base = 0
    temp = 1
    gap = 0

    while True:

        if temp > number:
            base = temp - gap
            break
        gap += 1 
        temp = temp +gap

    x = number - base +1
    y = gap - (number -base)

    return (x, y)


def new_calc(x, y):

   data1 = getPoint(x)
   data2 = getPoint(y)

   return getNumber(data1[0] +data2[0] , data1[1] +data2[1] )


T = int(input())

for t in range(1, T+1):
    p, q = map(int, input().split())

    print('#{} {}'.format(t, new_calc(p,q)))