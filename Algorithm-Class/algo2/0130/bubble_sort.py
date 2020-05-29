numbers = [55,7,78,12,42]


for i in range(len(numbers)-1,0,-1 ): #범위의 끝 위치 지정하는 for 문
    for j in range (0,i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1] , numbers[j]

    print(numbers)

print('Bubble Sorted => ', numbers)