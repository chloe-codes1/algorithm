T = int(input())
​
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
​
visited = [[False] * N for _ in range(N)]
sections = []
​
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        if board[i][j]:
            sections.append([i, j])
            # 세로 확인
            if i + 1 >= N:
                sections[-1].append(i)
            else:
                for k in range(i + 1, N):
                    if not board[k][j]:
                        sections[-1].append(k - 1)
                        break
                else:
                    sections[-1].append(k)
            # 가로 확인
            if j + 1 >= N:
                sections[-1].append(j)
            else:
                for k in range(j + 1, N):
                    if not board[i][k]:
                        sections[-1].append(k - 1)
                        break
                else:
                    sections[-1].append(k)
            for r in range(sections[-1][0], sections[-1][2] + 1):
                for c in range(sections[-1][1], sections[-1][3] + 1):
                    visited[r][c] = True

for section in sections:
    r1, c1, r2, c2 = section[0], section[1], section[2], section[3]
    section.append((r2 + 1 - r1) * (c2 + 1 - c1))

sections_sort = sorted(sections, key=lambda section: (section[-1], section[2] - section[0] + 1))

print('#{} {}'.format(tc, len(sections)), end=' ')
for section in sections_sort:
    print('{} {}'.format(section[2] - section[0] + 1, section[3] - section[1] + 1), end=' ')
