# 주어진 숫자만큼 # 을 출력해보세요.

# 주어질 숫자는 100,000 이하다.

num = int(input())
 

if num <= 100000:
    for _ in range(num):
        print('#',end='')