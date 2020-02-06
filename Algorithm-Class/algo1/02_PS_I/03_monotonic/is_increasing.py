
n = 1357

# 단조증가 하는지 체크하는 함수 check()

def check(n):
    n, r = n // 10, n % 10

    digits = []
    while n!=0:
        if n % 10 > r:
            returnFalse

        n, r = n//10, n%10
    
    digits.append(r)


    return True



print(check(n))