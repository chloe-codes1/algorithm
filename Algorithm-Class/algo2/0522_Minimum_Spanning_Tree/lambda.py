A = [[2,5], [5,2], [7,5], [3,2]]
A.sort()
print(A)
A.sort(key=lambda x:x[1])
print(A)