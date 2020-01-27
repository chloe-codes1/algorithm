# "기러기" 또는 "level" 과 같이 거꾸로 읽어도 앞에서부터 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

# 주어진 8x8 평면 글자판에서 가로, 세로를 모두 보아 제시된 길이를 가진 회문의 총 개수를 구하는 문제이다.
 



# 위와 같은 글자판이 주어졌을 때, 길이가 5인 회문은 붉은색 테두리로 표시된 4개가 있으며 따라서 4를 반환하면 된다.


# [제약 사항]

# 각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.

# 글자 판은 무조건 정사각형으로 주어진다.

# ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.

# 가로, 세로 각각에 대해서 직선으로만 판단한다.

# 즉, 아래 예에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.




# [입력]

# 각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가 주어지며, 다음 줄에 테스트 케이스가 주어진다.

# 총 10개의 테스트 케이스가 주어진다.


# [출력]

# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 개수를 출력한다.
size = 8

for t in range(1,11):
    length = int(input())

    array = [[]* s for s in range(size)]
    for s in range(size):
        array[s] = list(input())

    count = 0

    #가로
    for i in range(size):
        for j in range(size):
            if j-1 < size - length:  
                result = True 
                for m in range (length//2):
                    if array[i][j+m] != array[i][length +j-m -1]:
                        result = False
                        break
                if result:
                    count +=1

    #세로
    for i in range(size):
        for j in range(size):
            if i-1 < size - length:  
                result = True 
                for m in range (length//2):
                    if array[i+m][j] != array[length +i-m-1][j]:
                        result = False
                        break
                if result:
                 count +=1
    print('#{0} {1}'.format(t, count))