# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.

# 입력
# 첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N, 다음 줄에 N개의 0과1로 구성된 수열이 공백없이 제공된다.
# 1<=T<=10, 10<=N<=1000

# 출력
# #과 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

# 입력 예
# 3
# 10
# 0011001110
# 10
# 0000100001
# 10
# 0111001111

# 출력 예
# #1 3
# #2 1
# #3 4


T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = input()

    max_continuous = 0
    for i in range(N):
        if numbers[i] == '1':
            continuous = 1
            for j in range(1, N -i):
                if numbers[i+j] == '1':
                    continuous += 1
                else:
                    break
            if max_continuous < continuous:
                max_continuous = continuous
    
    print('#{} {}'.format(t, max_continuous))
        
