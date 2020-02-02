# 1 이상 100만(106) 이하의 모든 소수를 구하는 프로그램을 작성하시오.

# 참고로, 10 이하의 소수는 2, 3, 5, 7 이다.

# [입력]

# 이 문제의 입력은 없다.

# [출력]

# 1 이상 100만 이하의 소수를 공백을 사이에 두고 한 줄에 모두 출력한다.

import math

def find_all_primes(n):
    sieve = [True] *n
    
    i = 2
    while i<= int(math.sqrt(n)):
        



print(*find_all_primes(13))