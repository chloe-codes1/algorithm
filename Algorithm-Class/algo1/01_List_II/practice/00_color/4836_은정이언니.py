

T = int(input())
for tc in range(1, T+1):
    section_num = int(input())
    red = set()
    blue = set()
    for section in range(section_num):
        corner1_x, corner1_y, corner2_x, corner2_y, color = map(int, input().split())
        for x in range(corner1_x, corner2_x+1):
            for y in range(corner1_y, corner2_y+1):
                if color == 1:        
                    red.add((x, y))
                elif color == 2:
                    blue.add((x, y))
    purple = red & blue
    print(f'#{tc} {len(purple)}')