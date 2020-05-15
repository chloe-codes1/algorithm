# {1,2,3,4,5,6,7,8,9,10} 의 powerset 중 원소ㅡ이 값이 10인 부분집합을 모두 출력하시오.
def powerset(n, K, s, M, rs):
    global cnt
    if n == K:
        if s == M:






arr = [1,2,3,4,5,6,7,8,9,10]
M = 10
K = len(arr)
selected = [0]*K

powerset(0,K,0, M, sum(arr))