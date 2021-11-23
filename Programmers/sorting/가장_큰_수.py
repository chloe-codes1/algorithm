def solution(numbers):
    # 각각의 원소를 string으로 변환
    numbers = list(map(str, numbers))

    # 원소는 1000 이하 이므로 각각의 원소를 3자리 수 이상으로 맞춘 후, 문자열 비교 (ASCII 값으로 치환되어 정렬됨)
    numbers.sort(key=lambda x: x*3, reverse=True)

    # 모든 원소가 0일 경우, 000이 되는 경우를 방지하기 위해 int로 변환 후 다시 string으로 변
    return str(int(''.join(numbers)))


ret = solution([6, 10, 2])
print(ret)  # 6210

ret = solution([3, 30, 34, 5, 9])
print(ret)  # 9534330

ret = solution([0, 0, 0])
print(ret)  # 0
