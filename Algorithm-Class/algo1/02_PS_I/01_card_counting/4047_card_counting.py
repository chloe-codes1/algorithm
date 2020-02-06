

T = int(input())

for t in range(1, T+1):
    deck = {'S': 13, 'D':13,'H':13, 'C':13 }
    data = input()
    inHand = []
    for i in range(len(data)):
        if data[i] in 'SDHC':
            inHand.append(data[i:i+3])


    status = True

    check = []

    for hand in inHand:
        if hand in check:
            status = False
            break
        check.append(hand)

    for hand in inHand:    
        if hand[0] in deck.keys():
            if 1 <= int(hand[1:]) <=13:
                deck[hand[0]] -= 1      

    if status:
        print('#{}'.format(t), *[value for value in deck.values() ] )
    else:
        print('#{} ERROR'.format(t))