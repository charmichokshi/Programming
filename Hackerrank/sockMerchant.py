import os

'''
Return the total number of matching pairs of socks that John can sell.
i/p:
9
10 20 20 10 10 30 50 10 20
o/p:
3
'''
def sockMerchant(n, ar):
    hash_tbl = dict()
    no_of_pairs = 0
    for i in range(0, n):
        if ar[i] in hash_tbl.keys():
            hash_tbl[ar[i]] += 1
        else:
            hash_tbl[ar[i]] = 1

    for i in hash_tbl.keys():
        no_of_pairs += hash_tbl[i]/2

    return no_of_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(raw_input())
    ar = map(int, raw_input().rstrip().split())
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
