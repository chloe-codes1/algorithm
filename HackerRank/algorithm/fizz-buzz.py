#!/bin/python3

# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

THREE = 3
FIVE = 5
FIZZ_BUZZ = "FizzBuzz"
FIZZ = "Fizz"
BUZZ = "Buzz"


def fizzBuzz(n):
    # Write your code here
    for number in range(1, n + 1):
        if number % (THREE * FIVE) == 0:
            print(FIZZ_BUZZ)
        elif number % 3 == 0:
            print(FIZZ)
        elif number % 5 == 0:
            print(BUZZ)
        else:
            print(number)


if __name__ == '__main__':
    n = int(input().strip())  # 15

    fizzBuzz(n)
