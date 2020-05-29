arr = [[0,0,0,0,0],
       [0,0,1,0,3],
       [0,2,5,0,1],
       [4,2,4,4,2],
       [3,5,1,3,1]]
do = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for v in range(len(board)):
            val = board[v][m-1]
            if not val:
                continue
            else:
                if stack:
                    if stack[-1] == val:
                        stack.pop()
                        answer +=2
                    else:
                        stack.append(val)
                else:
                    stack.append(val)
                board[v][m-1] = 0
                break
    return answer

print(solution(arr,do))