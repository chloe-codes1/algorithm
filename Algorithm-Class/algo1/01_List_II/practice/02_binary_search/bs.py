
def find (total, target):
    l = 1
    r = total
    m = int((l+r)/2)  #int()도 // 몫 연산자와 같이 부동소수점 이하를 버려줌

    cnt = 1

    #중간값과 찾는 값이 같아질 때 까지 반복
    while m != target:
        if m < target:
            l = m
        else:
            r = m

        m = int((l+r)/2)
        cnt +=1

    return cnt




print(find(10,3))