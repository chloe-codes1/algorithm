<<<<<<< HEAD

brackets = [ '(', ')', '[', ']']

data = list(input().split('.'))

print(data)
=======
from collections import deque

brackets = { '(': ')', '[': ']' }
datas = []


while True:
    data = input()
    if data == '.':
        break
    datas.append(data)



for i in range(len(datas)):

    stack = deque()
    result = 'yes'
    for d in datas[i]:
        if d in brackets.keys():
            stack.append(d)
        elif d in brackets.values():
            if stack:
                popped = stack.pop()
                if brackets[popped] != d:
                    result ='no'
                    break
            else:
                result = 'no'
                break
    if stack:
        result = 'no'

    print(result)
>>>>>>> d193c42f3c50f72ca23f79db75dadc8fbefedb0e
