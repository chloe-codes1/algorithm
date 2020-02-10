

matches = { 0: 5, 1: 3, 2: 4}




N = int(input())

dices = [ list(map(int, input().split())) for _ in range(N)]


max_sum = 0

for i in range(6):
    selected = []
    side = dices[0][i]
    count = 0
    for key, val in matches.items():
        if key == i:
            opposite = dices[0][val]
        if val == i:
            opposite = dices[0][key]
    
    if side not in selected.keys():
        selected.update({side: 1})
    else:
        selected[side] +=1

    if opposite not in selected.keys():
        selected.update({opposite: 1})
    else:
        selected[opposite] +=1


    row = 1
    while True:

        if row > N-1:
            break
        side = opposite
        opposite = dices[row][ dices[row].index(side)]
        row +=1

        if side not in selected.keys():
            selected.update({side: 1})
        else:
            selected[side] +=1

        if opposite not in selected.keys():
            selected.update({opposite: 1})
        else:
            selected[opposite] +=1


    print(selected)



    if count > max_sum:
        max_sum = count


print('max_sum~~~ ㅎ_ㅎ', max_sum)