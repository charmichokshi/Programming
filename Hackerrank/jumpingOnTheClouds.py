import os

'''
Print the minimum number of jumps needed to win the game.
i/p:
7
0 0 1 0 0 1 0
o/p:
4
'''
def jumpingOnClouds(c):
    steps, next_check = 0, 0
    for i in range(0, len(c)):
        try:
            if c[i+next_check+2] == 1:
                steps += 1
                next_check += 0
            else:
                steps += 1
                next_check += 1
        except:
            if i+next_check+2 == len(c):
                steps += 1

    return steps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(raw_input())
    c = map(int, raw_input().rstrip().split())
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
