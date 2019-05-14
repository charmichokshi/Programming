#!/bin/python3

import os


'''
Print a single line of n space-separated integers denoting the final state of the array after performing d left rotations.

i/p:
5 4
1 2 3 4 5

o/p:
5 1 2 3 4
'''

def rotLeft(a, d):
    len_a = len(a)
    for i in range(0, d):
        a.append(a[i])
    return a[d:]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rotLeft(a, d)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
