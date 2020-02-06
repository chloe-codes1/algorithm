T = int(input())
for t in range(1, T+1):
    words = [input() for _ in range(5)]
    longest = 0

    for i in range(5):
        length = len(words[i])
        if length >longest:
            longest = length

    result = []
    for x in range(longest):
        for y in range(5):
            if x +1 <= len(words[y]):
                result.append(words[y][x])

    print('#{} {}'.format(t, ''.join(result)))