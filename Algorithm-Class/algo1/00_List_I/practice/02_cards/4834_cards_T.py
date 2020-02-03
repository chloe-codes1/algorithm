# Pythonic 하게 collections의 Counter 사용하기
# : Counter 는 모든것을 셀 수 있음! 문자도!

from collections import Counter


import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    d = list(input())

    c = Counter(d).most_common()

    #Counter().most_common 은 tuple로 이루어진 list를 return  => 그런데 이렇게 하면 key가 큰 순으로 sort 되지 않음

    #sorted(c.elements()) # ->가장 빈번하게 나오는 값들이 뒤쪽에 있게 sort 됨

    max_num = c[0][1]
    max_cards = [x for x, y in c if y == max_num]
    print(f'#{t} {max(max_cards)} {max_num}')
