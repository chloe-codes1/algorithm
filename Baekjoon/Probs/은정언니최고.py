# 개미문제


W, H = map(int, input().split())
c, r = map(int, input().split())
t = int(input())
nc = c+t
nr = r+t
c_q, c_r = divmod(nc, W)
if c_q % 2:
    c_final = W - nc % W
else:
    c_final = nc % W
r_q, r_r = divmod(nr, H)
if r_q % 2:
    r_final = H - nr % H
else:
    r_final = nr % H
print(c_final, r_final)
