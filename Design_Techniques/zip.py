a = [ [1,2,3,], ['a','b','c'], [ 0,0,0]]


#zip으로 전체 열 뽑기
print(list(zip(*a)))
# [(1, 'a', 0), (2, 'b', 0), (3, 'c', 0)]

#zip으로 특정 열 뽑기
print(list(zip(*a))[2])

# comprehension으로 전체 열 뽑기
print( [ [array[i] for array in a] for i in range(3) ]  )

# comprehension으로 특정 열 뽑기
print( [array[2] for array in a])