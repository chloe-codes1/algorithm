# arr = list()
# arr[0] =1
# -> 에러남
#    why? list를 생성만 해서 리스트의 주소만 갖고있고, 가리키는 리스트가 없기 때문!


arr = [0] *10
arr[0] = 1
arr[3] = 10
arr[9] =50

print(arr)