"""
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
"""


def solution(answers):
    result = []

    losers = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
     }

    total_question, winner_score = len(answers), float('-inf')
    for loser, pattern in losers.items():
        pattern_num = len(pattern)

        if pattern_num < total_question:
            quotient = total_question // pattern_num
            losers[loser] *= quotient + 1

        correct_answer = [i for i, v in enumerate(answers) if v == losers[loser][i]]
        score = len(correct_answer)

        if score > winner_score:
            result = [loser]
            winner_score = score

        elif score == winner_score:
            result += [loser]

    return result


ret = solution([1, 2, 3, 4, 5])
print(ret)  # 1
