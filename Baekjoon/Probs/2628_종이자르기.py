

col, row = map(int, input().split())

N = int(input())

rows = [0, row]
cols = [0, col]

for n in range(N):
    which_one, cut = map(int, input().split())

    if which_one == 0:
        rows.append(cut)
    elif which_one == 1:
        cols.append(cut)


row_gap = 0
col_gap = 0

rows = sorted(rows)
cols = sorted(cols)


for r in range(len(rows) -1):
    gap = rows[r+1] -rows[r]
    if gap > row_gap:
        row_gap = gap


for c in range(len(cols) -1):
    gap = cols[c+1] - cols[c]
    if gap > col_gap:
        col_gap = gap

print(row_gap*col_gap)