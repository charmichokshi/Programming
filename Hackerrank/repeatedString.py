#!/bin/python

def repeatedString(s, n):
    len_s = len(s)
    cnt_a, cnt = 0, 0
    for char in s:
        if char == "a":
            cnt += 1

    if len_s < n:
        div = n / len_s
        mod = n % len_s
        sum = 0
        for i in range(mod):
            if s[i] == "a":
                sum += 1
        return div * cnt + sum
    else:
        sum = 0
        for i in range(n):
            if s[i] == "a":
                sum += 1
        return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
