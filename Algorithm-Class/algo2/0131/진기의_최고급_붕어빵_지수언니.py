# ver 3) 갓지수 언니 코드 훔쳐오긔

def make_goldfish(n, m, k, arriving_seconds):
    make = [0]
    for seconds in range(1, max(arriving_second)+1):
        if not seconds%m:
            make[0] += k
        if 0 in arriving_second:
            return 'Impossible'
        if seconds in arriving_seconds:
            if make[0]:
                make[0] -= arriving_second.count(seconds)
                if make[0] < 0:
                    return 'Impossible'
            else:
                return 'Impossible'
    return 'Possible'
test = int(input())
for t in range(1, test+1):
    n, m, k = map(int,input().split())
    arriving_second = list(map(int, input().split()))
    result = make_goldfish(n, m, k, arriving_second)
    print(f'#{t} {result}')