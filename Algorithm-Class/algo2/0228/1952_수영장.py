
T = int(input())
result = [0]*T  #이거 그냥 한번에 출력용! (속도 안빨라짐 ㅎ_ㅎ 놀랍도록 똑같음)

def min_fee(month, fee):
    global total
    if month > 12:
        if total > fee:
            total = fee
    else:
        for i in range(3):
            if i == 0: # period[0] == 1일일때!
                min_fee(month +periods[i], fee + (fees[i]*infos[month])) #기간 중 1일 요금일때만 해당 월 일수만큼 곱하기
            else:
                min_fee(month +periods[i], fee + fees[i]) #1달, 3달일땐 그냥 요금 더하기

for t in range(T):
    fees = list(map(int, input().split()))
    infos = [0] + list(map(int, input().split())) #0월은 없으므로 [0] 넣어서 index랑 월 맞추깅
    periods = [1,1,3] #1일, 1달, 3달
    total = fees[3] #연 요금을 total 초기값으로 넣기
    min_fee(1,0) #index 맞춰줬으므로 1월부터 그대로 시쟉
    result[t] = total #한번에 출력용...

for r in range(T):
    print('#{} {}'.format(r+1, result[r]))

