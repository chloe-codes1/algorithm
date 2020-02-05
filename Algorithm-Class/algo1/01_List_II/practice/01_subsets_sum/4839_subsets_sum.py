# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

# 해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
 

# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

 
 

# [입력]
 

# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
 

# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

 

# [출력]
 

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.






import itertools

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    
    array = [i for i in range(1,13) ]

    count = 0
    arrays = list(itertools.combinations(array[:K - (N-1)*N//2 ], N))
                                            # 불필요하게 이미 K가 넘는 수를 빼려고 slicing (은정이언니 아이디어)

    for j in arrays:
        if sum(j) == K:
                count+=1                   
    print('#{} {}'.format(t,count))
