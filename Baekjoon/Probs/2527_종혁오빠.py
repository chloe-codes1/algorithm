ac1, ar1, ac2, ar2, bc1, br1, bc2, br2 = map(int, input().split())
A = [ac1, ar1, ac2, ar2]
B = [bc1, br1, bc2, br2]
if ac1 > bc1 :
    A, B = B, A
res = ''
# case d) 닿지 않는 경우
# 위 or 오른쪽 or 아래
if ar2 < br1 or ac2 < bc1 or br2 < ar1:
    res = 'd'
# case b) 선으로 접하는 경우
else:
    # 위
    if ar2 == br1 and ac1 <= bc1 < ac2:
        res = 'b'
    # 오른
    elif ac2 == bc1 and br2 > ar1 and br1 < ar2:
        res = 'b'
    # 아래
    elif ar1 == br2 and ac1 <= bc1 < ac2:
        res = 'b'
    # case c) 점으로 닿는 경우
    else:
        if ar2 == br1 and ac2 == bc1:
            res = 'c'
        elif ar1 == br2 and ac2 == bc1:
            res ='c'
        else:
            res ='a'
print(res)