
import sys 

sys.stdin = open('input.txt')


T = int(input())

for t in range(1, T+1):
    text = input()
    length = len(text)

    print('..' +  '...'.join('#'*length) + '..')
    print('.#' + '#.#'.join('.'*length) + '#.')
    print('#.' + '.#.'.join(text) + '.#')
    print('.#' + '#.#'.join('.'*length) + '#.')
    print('..' +  '...'.join('#'*length) + '..')