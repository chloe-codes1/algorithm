# 문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

# 예를 들어

# “3+(4+5)*6+7”

# 라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.

# "345+6*+7+"

# 변환된 식을 계산하면 64를 얻을 수 있다.

# 문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.

# 이 때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.

# 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

# [입력]

# 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.

# 총 10개의 테스트 케이스가 주어진다.

# [출력]

# # 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.




T = 10
for t in range(1, T+1):
    length = int(input())
    formula = input()

    stack = []  #숫자 저장
    temp = []   #연산자 저장

    weight = {'*':2, '+':1, '(':3}
    temp_weight = {'*':2, '+':1, '(':0} 

    # Step 1: 중위표기법  -> 후위 표기법
    for i in range(length):
        if formula[i].isdigit():
            stack.append(formula[i])
        else:
            if not temp:
                temp.append(formula[i])
            else:
                if formula[i] == ')':
                    while temp[-1] != '(':
                        stack.append(temp.pop())
                    temp.pop() # 여는 괄호 없애긔
                else:
                    while weight[formula[i]] <= temp_weight[temp[-1]]:
                        stack.append(temp.pop())
                    temp.append(formula[i])

    # Step 2 : 후위표기법 수식 계산
    for s in stack:
        if s.isdigit():
            temp.append(s)
        else:
            num2 = temp.pop()
            num1 = temp.pop()
            if s == '*':
                temp.append(int(num1)*int(num2))
            elif s == '+':
                temp.append(int(num1) + int(num2))
    
    print('#{} {}'.format(t,temp[0]))

                


                                


                


