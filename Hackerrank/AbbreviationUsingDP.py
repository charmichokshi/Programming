def abbreviation(a, b):
    if len(b) > len(a):
        return("NO")
    else:
        i = 0
        j = 0
        n = len(a)
        dp = [False for x in range(len(b))] 
        
        while i < n:
            found = False
            while i < n and a[i].upper() != b[j]:
                if a[i].isupper() and b[j-1] != a[i]:
                    return("NO")
                i = i + 1
        
            if i < len(a):
                found = True
            if found:
                dp[j] = True
                j = j + 1
                if j == len(b):
                    break
            i = i + 1
        
        if dp[-1]:
            for c in a[i+1:]:
                if c.isupper() and b[j-1] != c:
                    return("NO")    
            return("YES")
        else:
            return("NO")
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        a = input()
        b = input()
        result = abbreviation(a, b)
        fptr.write(result + '\n')
    fptr.close()
