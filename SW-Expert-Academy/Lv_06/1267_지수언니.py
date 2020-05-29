T = 3
for t in range(1, T+1):

    vertex, edge = map(int, input().split())
    orders = list(map(int, input().split()))

    start = [ orders[b] for b in range(edge*2) if not b%2 ]
    end = [ orders[a] for a in range(edge*2) if a%2 ]
    
   
    result = []
    temp = [0]*(vertex + 1)
    while len(result) < vertex:
        for idx in range(len(start)):
            if start[idx] in result:
                if end.count(end[idx]) == 1 and end[idx] not in result:
                    result.append(end[idx])
            else:
                if start[idx] not in end:
                    result.append(start[idx])
                    if end.count(end[idx]) == 1 and end[idx] not in result:
                        result.append(end[idx])
                    else:
                        temp[end[idx]] += 1
        for idx2 in range(len(end)):
            if end[idx2] not in result and temp[end[idx2]] == end.count(end[idx2]):
                result.append(end[idx2])

        for idx3 in range(len(start)):
            if start[idx3] in result and end[idx3] in result:
                start.pop(idx3)
                end.pop(idx3)

    print(*result) 