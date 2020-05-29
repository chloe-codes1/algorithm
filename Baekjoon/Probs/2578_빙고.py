bingo = [ list(map(int, input().split())) for _ in range(5)]


calls = []

for _ in range(5):
    calls.extend( map(int,input().split()))


for c in range(len(calls)):
    count = 0
    result = 0
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == calls[c]:
                bingo[i][j] = 0
                
                for row in range(5):
                    if sum(bingo[row]) == 0:
                        count += 1

                for col in range(5):
                    isZero = True
                    for row in range(5):
                        if bingo[row][col] !=0:
                            isZero = False
                            break
                    if isZero:
                        count +=1
                
                isZero = True
                for l in range(5):
                    if bingo[l][l] != 0:
                        isZero = False
                        break
                if isZero:
                    count+=1
                
                isZero = True
                for r in range(4, -1, -1):
                    if bingo[r][4-r] != 0:
                        isZero = False
                        break
                if isZero:
                    count+=1                

                if count >=3:
                    result = c
                    break
            
        if result:
            break
    if result:
        break

print(result+1)            





