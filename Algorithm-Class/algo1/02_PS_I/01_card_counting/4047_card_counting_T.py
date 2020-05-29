import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    cards = input()
    hands = {'S':[], 'D': [], 'H': [], 'C': []}

    for n in range(len(cards) //3):
        shape = cards[n*3]
        number = cards[n*3 +1 : n*3 +3]

        if number not in hands[shape] :
            hands[shape].append(number)
        else:
            print('#{} ERROR'.format(t))
            break

    # for문이 다 돌아야지만!!! 수행되는 else
    else:
        result = [13 -len(c) for c in hands.values()]

    print('#{}'.format(t), *result)