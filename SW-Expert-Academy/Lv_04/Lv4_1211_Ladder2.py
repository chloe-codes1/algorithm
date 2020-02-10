T =10
for t in range(1, T+1):
    case = int(input())
    ladder = [ list(map(int,input().split())) for _ in range(100) ]


    min_count = 10000
    min_index = 0


    for i in range(100):
        count = 0
        
        row = 0
        if ladder[row][i] == 1:
            row += 1
            count+=1             
            
            col = i
            direction = ''
            while row < 100:
                if col <99 and ladder[row][col+1] == 1 and direction != 'left':
                    j = col +1
                    direction = 'right'

                    while j <100:
                        if ladder[row][j] == 0:
                            break
                        j+=1
                        count+=1
                    
                    col = j -1

                elif col > 0 and ladder[row][col-1] == 1 and direction != 'right':
                    j = col -1
                    direction = 'left'
                    while j >= 0:
                        if ladder[row][j] == 0:
                            break
                        j -= 1
                        count+=1
                    
                    col = j +1

                elif ladder[row][col] == 1:
                    row += 1
                    count+=1
                    direction = ''


            if min_count > count:
                min_count = count
                min_index = i
            elif min_count == count and min_index <i:
                min_index = i
            

    print('#{} {}'.format(t, min_index))