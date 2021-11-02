# 효율성 개선

def solution(phone_book):
    answer = True
    count = len(phone_book)
    # sort()로 오름차순으로 정렬
    phone_book.sort()
    for idx, val in enumerate(phone_book):
        length = len(val)
        # 해당 idx 이후만 순회 하도록 설정
        for i in range(idx+1, count):
            # prefix가 같아야 하므로, 전화 번호의 시작이 다르면 continue
            if val[0] != phone_book[i][0]:
                continue
            # 길이가 더 길다는 것은 prefix가 같지 않다는 것 이므로 break
            if length >= len(phone_book[i]):
                break
            if val == phone_book[i][:length]:
                answer = False
                return answer
    return answer
