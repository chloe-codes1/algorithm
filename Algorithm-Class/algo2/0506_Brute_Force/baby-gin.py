# 6자리 숫자에 대해서 완전 검색을 적용해서 Baby-gin을 검사해보시오.

# [baby-gin]
# 1. 3장의 카드 연속적 - run
# 2. 3장의 카드 동일한 번호 -triplet
# 3. run과 triplet 으로만 구성 된 경우 baby-gin


"""
입력 예

124783
667767
054060
101123
"""




data = input()
front = data[:3]
back = data[3:]
