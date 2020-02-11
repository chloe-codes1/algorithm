
K = int(input())

infos = []

widths = []
heights = []


for _ in range(6):
    direction, length = map(int, input().split())
    infos.append([direction, length])
    if direction == 1 or direction == 2:
        widths.append(length)
    elif direction == 3 or direction ==4:
        heights.append(length)

entire = max(widths) * max(heights)
blank =0

infos += infos[:3]


for i in range(len(infos)):
    if infos[i][0] == infos[i+2][0] and infos[i+1][0] == infos[i+3][0]:
        blank = infos[i+1][1] * infos[i+2][1]
        break

print( (entire - blank)*K)
