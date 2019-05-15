#!/bin/python3

import os


def find(target, myList):
    for i in range(len(myList)):
        if myList[i] == target:
            return i


def minimumSwaps(arr):
    swap = 0
    skip_index = list()
    for i in range(len(arr)):
        if i not in skip_index:
            if i+1 != arr[i]:
                # i: curr element index
                # j: index of element which should be at this place
                # k: correct index of the curr element
                j = find(i+1, arr)
                k = arr[i]-1

                arr[i], arr[j] = arr[j], arr[i]
                skip_index.append(i)

                if j+1 != arr[j]:
                    arr[k], arr[j] = arr[j], arr[k]
                    swap += 2
                    skip_index.append(k)
                else:
                    swap += 1
    return swap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
