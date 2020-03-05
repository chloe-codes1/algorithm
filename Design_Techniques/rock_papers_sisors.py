# 항래님이 알려주신 가위바위보!

####가위:1, 바위:2, 보:3
# 1<2, 2<3, 3<1
def rsf1(a,b):
    if a==b:
        return 'draw'
    elif a%3+1 == b:
        return b
    else:
        return a
###가위:0, 바위:1, 보:2 (인덱스로 활용할 때)
# 0<1, 1<2, 2<0
def rsf2(a,b):
    if a==b:
        return 'draw'
    elif (a+1)%3 == b:
        return b
    else:
        return a



# 은정언니가 알려준것!!

# (a-b+3)%3 == 1:a 승리
# (a-b+3)%3 == 2 : a 패배 