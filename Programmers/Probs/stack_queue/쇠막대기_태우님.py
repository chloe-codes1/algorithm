def solution(arrangement):
    answer = 0
    stack = 0
    for index, i in enumerate(arrangement):
        if i == ')' :
            stack -= 1 #레이저 닫는 괄호
            if arrangement[index-1] == ')': # 나머지 닫는 괄호
                answer += 1
            else:
                answer += stack
        else:
            stack += 1
    return answer



print(solution('()(((()())(())()))(())'))