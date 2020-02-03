# ver1) 내 답

for t in range (1,11):
    dump_count = int(input())
    boxes = list(map(int, input().split()))
    sorted_boxes = sorted(boxes)
    for _ in range(dump_count):
        sorted_boxes = sorted(sorted_boxes)
        if sorted_boxes[99] - sorted_boxes[0] < 0:
            break
        sorted_boxes[0] += 1
        sorted_boxes[99] -= 1
    sorted_boxes = sorted(sorted_boxes)
    print('#{0} {1}'.format(t, sorted_boxes[99] - sorted_boxes[0]))

