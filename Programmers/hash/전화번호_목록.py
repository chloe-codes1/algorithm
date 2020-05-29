def solution(phone_book):
    answer = True
    count = len(phone_book)
    for idx, val in enumerate(phone_book):
        length = len(val)
        for i in range(count):
            if idx != i:
                if val == phone_book[i][:length]:
                    answer = False
                    return answer
    return answer