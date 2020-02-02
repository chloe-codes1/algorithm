# 1 이상 100만(106) 이하의 모든 소수를 구하는 프로그램을 작성하시오.

# 참고로, 10 이하의 소수는 2, 3, 5, 7 이다.

# [입력]

# 이 문제의 입력은 없다.

# [출력]

# 1 이상 100만 이하의 소수를 공백을 사이에 두고 한 줄에 모두 출력한다.

def find_all_primes(n):
    if n < 2:
        return []
    s = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    return [i for i, v in enumerate(s) if v]


print(*find_all_primes(1000000))