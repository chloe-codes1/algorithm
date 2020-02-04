# 원형 금속 막대를 가장 길게 연결하고자 한다. 원형 금속 막대는 한 쪽 면에 수나사와 다른 쪽에 암나사로 이루어져 있다.

# 수나사와 암나사는 굵기가 서로 다르다. 아래 그림에서 수나사의 굵기는 3을 암나사의 굵기는 4를 나타내고 있다.

# 이후 나사의 굵기를 수나사의 굵기 x 암나사의 굵기로 표현한다. 연결은 +로 표현한다.
 

 

# 이와 같은 원형 금속 막대를 연결하기 위해서는 수나사의 굵기와 암나사의 굵기가 서로 일치해야 한다.

# 예를 들어 두 개의 원형 금속 막대 3x4와 4x5가 있을 때 3x4+4x5로 연결해야 연결되며 4x5+3x4로 연결하면 연결되지 않는다.
 


# 수나사와 암나사의 크기가 서로 다른 여러 개의 원형 금속 막대를 가장 많이 연결하려고 한다.

# 어떤 순서로 연결해야 가장 많이 연결하는지를 찾는 프로그램을 작성하시오.

# [입력]

# 맨 첫 줄에는 테스트 케이스의 개수가 주어진다.

# 그리고 테스트 케이스가 각 라인에 주어진다. 각 테스트 케이스는 2줄로 구성되며, 첫 줄에는 원형 금속 막대의 개수 n이 주어지고, 다음 줄에는 2n개의 수가 주어진다. 

# 숫자는 공백으로 구분한다. 앞에서부터 2개씩 하나의 원형 금속 막대의 수나사 굵기와 암나사 굵기를 의미한다.
 
# [출력]

# 각 테스트 케이스 각각에 대한 답을 출력한다.

# 각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음, 각 테스트 케이스에 주어진 수열로부터 가장 많이 연결하기 위한 원형 금속 막대의 수나사 굵기와 암나사 굵기를 순서대로 출력한다.


T = int(input())

for t in range(1, T+1):
    n = int(input())

    screws = list(map(int, input().split()))

    m_screw = [ screws[a] for a in range(len(screws)) if not a%2 ]
    f_screw = [ screws[a] for a in range(len(screws)) if a%2 ]


    first = [ m for m in m_screw if m not in f_screw]
    last = [f for f in f_screw if f not in m_screw]


    first_idx = m_screw.index(first[0])
    first.append( f_screw[first_idx])
    m_screw.pop(first_idx)
    f_screw.pop(first_idx)

    last_idx = f_screw.index(last[0])
    last.insert( 0, m_screw [last_idx])
    m_screw.pop(last_idx)
    f_screw.pop(last_idx)


    print(first)
    print(last)
    print(m_screw)
    print(f_screw)

    while True:
        if len(m_screw) == 0 or len(f_screw) ==0:
            break

        for i in range(len(m_screw)):
            if m_screw[i] == first[-1]:
                first.append(m_screw[i])
                first.append(f_screw[i])
                m_screw.pop(i)
                f_screw.pop(i)
    
    result = first + last
    print(result)



    




    # for i in range(len(screws) -3):
    #     if screws[i] == first[0] and screws[i+1] ==first[1]:
    #         print('롸?')
    #         screws.pop(i)
    #         screws.pop(i)
        
    #     if screws[i] == last[0] and screws[i+1] ==last[1]:
    #         screws.pop(i)
    #         screws.pop(i)

    # print(screws)



