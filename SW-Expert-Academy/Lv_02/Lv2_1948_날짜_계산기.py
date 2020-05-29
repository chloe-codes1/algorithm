# 월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.


# [제약 사항]

# 월은 1 이상 12 이하의 정수이다. 각 달의 마지막 날짜는 다음과 같다.

# 1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31

# 두 번째 날짜가 첫 번째 날짜보다 항상 크게 주어진다.


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.

# 첫 번째 수가 월을 나타내고 두 번째 수가 일을 나타낸다. 그 다음 같은 형식으로 두 번째 날짜가 주어진다.


# [출력]

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


T = int(input())
calendar = {'1':31, '2':28, '3':31,'4': 30, '5':31, '6':30, '7': 31, '8':31, '9':30, '10':31, '11': 30, '12':31}

for i in range(1,T+1):
    month1, day1, month2, day2 = input().split()

    if int(month1) - int(month2) != 0:
        result = 0
        
        for m in range(int(month2) - int(month1)):

            result += calendar[str(int(month1) + m)]

            print(calendar[str(int(month1) + m)])

        if int(day2) > int(day1):
            result += int(day2) - int(day1) +1
        else:
            result -= calendar[month1]
            result += calendar[month1] - int(day1) +1
            result += int(day2)
        print('#{0} {1}'.format(i,result))


    else:
        print('#{0} {1}'.format(i,int(day2)-int(day1) + 1))
        