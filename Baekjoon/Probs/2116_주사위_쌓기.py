
# ver1) 



matches = { 0: 5, 1: 3, 2: 4, 5:0, 3:1, 4:2}


N = int(input())

dices = [ list(map(int, input().split())) for _ in range(N)]


max_sum = 0

for i in range(6):
    count = 0

    selected = []
    options = [n for n in range(1,7)]
    side = dices[0][i]
    options.remove(side)
    opposite = dices[0][ matches[i]]
    options.remove(opposite)
    
    count += max(options)

    row = 1
    while True:
        options = [n for n in range(1,7)]
        if row >= N:
            break
        side = opposite
        options.remove(side)
        opposite = dices[row][ matches[i]]
        options.remove(opposite)
        
        count += max(options)
        row +=1


    if count > max_sum:
        max_sum = count


print('max_sum~~~ ㅎ_ㅎ', max_sum)



