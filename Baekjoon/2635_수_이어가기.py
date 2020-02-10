# 다음과 같은 규칙에 따라 수들을 만들려고 한다.

# 첫 번째 수로 양의 정수가 주어진다.
# 두 번째 수는 양의 정수 중에서 하나를 선택한다.
# 세 번째부터 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다. 예를 들어, 세 번째 수는 첫 번째 수에서 두 번째 수를 뺀 것이고, 네 번째 수는 두 번째 수에서 세 번째 수를 뺀 것이다.
# 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.
# 첫 번째 수로 100이 주어질 때, 두 번째 수로 60을 선택하여 위의 규칙으로 수들을 만들면 7개의 수들 100, 60, 40, 20, 20 , 0, 20이 만들어진다. 그리고 두 번째 수로 62를 선택하여 위의 규칙으로 수들을 만들면 8개의 수들 100, 62, 38, 24, 14, 10, 4, 6이 만들어진다. 위의 예에서 알 수 있듯이, 첫 번째 수가 같더라도 두 번째 수에 따라서 만들어지는 수들의 개수가 다를 수 있다.

# 입력으로 첫 번째 수가 주어질 때, 이 수에서 시작하여 위의 규칙으로 만들어지는 최대 개수의 수들을 구하는 프로그램을 작성하시오. 최대 개수의 수들이 여러 개일 때, 그중 하나의 수들만 출력하면 된다.

# 입력
# 첫 번째 수가 주어진다. 이 수는 30,000 보다 같거나 작은 양의 정수이다.

# 출력
# 첫 번째 줄에는 입력된 첫 번째 수로 시작하여 위의 규칙에 따라 만들 수 있는 수들의 최대 개수를 출력한다.

# 둘째 줄에 그 최대 개수의 수들을 차례대로 출력한다. 이들 수 사이에는 빈칸을 하나씩 둔다.



number = int(input())


max_count = 0
max_num = 0


# 전체를 탐색하니까 시간/메모리 초과되어서 범위 제한을 둠
for n in range(number//(5//4) , number//(5//2), -1):
    count = 2
    base = number
    takeaway = n
    num = base - takeaway
    while num >= 0:
        base = takeaway
        takeaway = num
        num = base - takeaway
        count +=1
    
    if max_count < count:
        max_count = count
        max_num = n

result = [number, max_num]

base = number
takeaway = max_num
num = base - takeaway

while num >= 0:
    result.append(num)
    base = takeaway
    takeaway = num
    num = base - takeaway


print(max_count)
print(*result)
        

