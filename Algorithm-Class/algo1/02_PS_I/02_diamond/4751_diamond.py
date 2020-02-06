T = int(input())

outer_start = '..#'
outer = '...#'
inner = '.#.#'

for t in range(1, T+1):
    word = input()

    if len(word) == 1:
        print(outer_start + '..\n' + inner +'.\n#.'+word +'.#\n'+inner + '.\n' + outer_start +'..')

    else:

        outer_result = outer_start + outer*(len(word) -1) + '..'
        inner_result = inner*len(word) + '.'

        result = '#.'
        for idx, val in enumerate(word):
            if idx !=0:
                result += '.'
            result += val
            result += '.#'

        print(outer_result + '\n' + inner_result + '\n' + result + '\n' + inner_result +'\n' + outer_result)

    
