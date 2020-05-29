# ver 1) ㅎㅎ...... 메모리 초과....ㅎㅎ



# for _ in range(4):
#     A_row1, A_col1, A_row2, A_col2, B_row1, B_col1, B_row2, B_col2 = map(int, input().split())
#     spots = [A_row1, A_col1, A_row2, A_col2, B_row1, B_col1, B_row2, B_col2]
#     size = max(spots) +1
#     board = [ list( [0]*size) for _ in range(size)]

#     for row in range(A_row1, A_row2 +1):
#         for col in range(A_col1, A_col2 +1):
#             board[row][col] += 1

#     for row in range(B_row1, B_row2 +1):
#         for col in range(B_col1, B_col2 +1):
#             board[row][col] += 2

#     result =''

#     isOverlapped = False

#     for row in range(size):
#         for col in range(size):
#             if board[row][col] ==3:
#                 isOverlapped =True
#                 break
#         if isOverlapped:
#             break

#     if isOverlapped:
#         result = 'a'
#     else:
#         result = 'd'


#     rows = [ spots[s] for s in range(8) if not s%2]
#     cols = [ spots[s] for s in range(8) if s%2]



#     duplicated_col = 0
#     for c in cols:
#         if cols.count(c) > 1:
#             duplicated_col = c
#             break

#     duplicated_row = 0
#     for r in rows:
#         if rows.count(r) > 1:
#             duplicated_row = r
#             break

#     if duplicated_col: 
#         following_row_A = 0
#         following_row_B = 0

#         A_half = spots[:4]
#         B_half = spots[4:]

#         for idx,val in enumerate(A_half):
#             if duplicated_col == val:
#                 following_row_A = spots[idx-1]
#                 break
#         for idx,val in enumerate(B_half):
#             if duplicated_col == val:
#                 following_row_B = spots[idx-1]
#                 break

#         A_is_bigger = True
#         if size in B_half:
#             A_is_bigger = False
#             break
        
#         if A_is_bigger:
#             if following_row_B > following_row_A:
#                 result = 'b'
#             else:
#                 result = 'c'
#         else:
#             if following_row_B < following_row_A:
#                 result = 'b'
#             else:
#                 result = 'c'

        
#     if duplicated_row: 
#         following_col_A = 0
#         following_col_B = 0

#         A_half = spots[:4]
#         B_half = spots[4:]

#         for idx,val in enumerate(A_half):
#             if duplicated_row == val:
#                 following_col_A = spots[idx-1]

#         for idx,val in enumerate(B_half):
#             if duplicated_row == val:
#                 following_col_B = spots[idx-1]

#         A_is_bigger = True
#         if size in B_half:
#             A_is_bigger = False
        
#         if A_is_bigger:
#             if following_col_B > following_col_A:
#                 result = 'b'
#             else:
#                 result = 'c'
#         else:
#             if following_col_B < following_col_A:
#                 result = 'b'
#             else:
#                 result = 'c'


#     print(result)

        


# ver 2) 형수님 최고..


for _ in range(4):

    A_col1, A_row1, A_col2, A_row2, B_col1, B_row1, B_col2, B_row2 = map(int, input().split())

    result = ''
    
    if A_col1 > B_col1:
        A_col1, B_col1 = B_col1, A_col1
        A_row1, B_row1 = B_row1, A_row1
        A_col2, B_col2 = B_col2, A_col2
        A_row2, B_row2 = B_row2, A_row2
    

    if A_col2 < B_col1:
        result = 'd'
    elif A_row2 < B_row1:
        result = 'd'
    elif A_row1 > B_row2:
        result = 'd'
    else:
        result = 'a'


    if A_row2 == B_row1:
        if A_col2 > B_col1:
            result = 'b'
        else:
            result = 'c'

    if A_col2 == B_col1:
        if A_row2 > B_row1:
            result = 'b'
        else:
            result = 'c'

    if B_row2 == A_row1:
        if B_col1 < A_col2:
            result = 'b'
        else:
            result = 'c'
    
    print(result)