
# ver1) 틀렸다고 전해라..


# from itertools import combinations

# dwarfs = [ int(input()) for _ in range(9)]

# results = list( combinations(dwarfs, 7) )

# found = []
# for result in results:
#     if sum(result) == 100:
#         found.extend(result)

# for f in sorted(found):
#     print(f)



# ver 2)

# dwarfs = [ int(input()) for _ in range(9)]

# total = sum(dwarfs)

# results = [True] *9

# for i in range(8):
#     for j in range(i +1 , 9):
#         if total - dwarfs[i] - dwarfs[j] == 100:
#             results[i] = False
#             results[j] = False
#             break

# answer =  sorted([dwarfs[i] for i in range(9) if results[i] == True ])

# for a in answer:
#     print(a)


# ver 3

dwarfs = [int(input()) for _ in range(9)]

total = sum(dwarfs)

answer = []

for i in range(8):
    for j in range(i+1, 9):
        if total - dwarfs[i] - dwarfs[j] == 100:
            answer = [dwarfs[k] for k in range(9) if k!=i and k!=j]
            break

answer.sort()

for a in answer:
    print(a)