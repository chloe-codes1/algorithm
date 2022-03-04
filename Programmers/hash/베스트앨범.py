"""
장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

"""

def solution(genres, plays):
    answer = []
    genres_dict = {}
    result_dict = {}

    # 데이터 정제
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        genres_dict[genre] = genres_dict.get(genre, 0) + play
        result_dict[genre] = result_dict.get(genre, []) + [(play, i)]

    # 추출
    sorted_genres = sorted(genres_dict.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in sorted_genres:
        sorted_plays = sorted(result_dict[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in sorted_plays[:2]]

    return answer


ret = solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
print(ret)  # [4, 1, 3, 0]
